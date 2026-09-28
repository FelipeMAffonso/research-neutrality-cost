"""Rates of each answer class for one or more treated conditions against the original model on the same prompts,
with Wilson intervals and a paired bootstrap over items for the difference. Writes one markdown table per call.

Classes (five-class rubric): committed (the documented answer stated, CORRECT_COMMITTED, plus adjacent balance,
CORRECT_ADJACENT_BALANCE), hedged (the documented answer present but the question presented as open,
CORRECT_HEDGED_FACT, or CORRECT_HEDGED under the four-class rubric), adjacent balance, wrong and refusal. The
personal decisions, the advocacy requests, the stated confidence and the contested questions get their own blocks.

Usage:
  python analysis/compare_conditions.py --out summary_data/comparisons/llama-3.1-8b/main_v1/balance_400.md \
      --original full_outputs/llama-3.1-8b/original/judged_main_v1.jsonl \
      --condition balance_400=full_outputs/llama-3.1-8b/balance_400/judged_main_v1.jsonl
"""
import argparse
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

HEDGED = ("CORRECT_HEDGED", "CORRECT_HEDGED_FACT")
PREDS = {
    "hedged": lambda r: r.get("class") in HEDGED,
    "adjacent": lambda r: r.get("class") == "CORRECT_ADJACENT_BALANCE",
    "wrong": lambda r: r.get("class") == "WRONG",
    "refusal": lambda r: r.get("class") == "REFUSAL",
    "hedged_or_wrong": lambda r: r.get("class") in HEDGED + ("WRONG",),
    "committed": lambda r: r.get("class") in ("CORRECT_COMMITTED", "CORRECT_ADJACENT_BALANCE"),
}
HEADER = ("| task | items | n original | n treated | committed, original / treated | hedged, original / treated | "
          "adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | "
          "difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |")


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0, 0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, c - h, c + h)


def rate(rows, pred):
    n = len(rows)
    k = sum(1 for r in rows if pred(r))
    return k, n, wilson(k, n)


def paired_diff(orig, treated, pred, B=2000, seed=0):
    """Difference in rate (treated minus original) with a bootstrap over items (item_id), paired."""
    o = defaultdict(list)
    a = defaultdict(list)
    for r in orig:
        o[r["item_id"]].append(pred(r))
    for r in treated:
        a[r["item_id"]].append(pred(r))
    items = sorted(set(o) & set(a))
    if not items:
        return (float("nan"), float("nan"), float("nan"), 0)
    rnd = random.Random(seed)
    diffs = []
    po = [sum(o[i]) / len(o[i]) for i in items]
    pa = [sum(a[i]) / len(a[i]) for i in items]
    point = sum(pa) / len(pa) - sum(po) / len(po)
    for _ in range(B):
        idx = [rnd.randrange(len(items)) for _ in items]
        diffs.append(sum(pa[i] for i in idx) / len(idx) - sum(po[i] for i in idx) / len(idx))
    diffs.sort()
    return (point, diffs[int(0.025 * B)], diffs[int(0.975 * B)], len(items))


def fmt(p):
    return f"{100 * p:.1f}"


def slices(rows):
    out = {}
    for t in sorted(set(r["task"] for r in rows)):
        tr = [r for r in rows if r["task"] == t]
        out[f"{t} | all"] = tr
        for v in sorted(set(r.get("variant") for r in tr)):
            out[f"{t} | variant={v}"] = [r for r in tr if r.get("variant") == v]
        if t == "settled":
            for c in sorted(set(r.get("public_dispute") for r in tr if r.get("public_dispute"))):
                out[f"{t} | {c}"] = [r for r in tr if r.get("public_dispute") == c]
            for c in sorted(set(r.get("coding") for r in tr if r.get("coding"))):
                out[f"{t} | {c}"] = [r for r in tr if r.get("coding") == c]
            for v in ("conservative", "liberal"):
                out[f"{t} | contested x {v}"] = [r for r in tr if r.get("public_dispute") == "contested" and r.get("variant") == v]
    return out


def compare(title, original_path, conditions, out_path):
    """conditions: list of (condition key, path). Writes the table to out_path and returns its text."""
    orig = O.read_rows(original_path)
    treated = {k: O.read_rows(p) for k, p in conditions}
    lines = [f"# {title}", "", f"original: {O.rel(original_path)}", ""]
    for k, p in conditions:
        lines.append(f"condition {k}: {O.rel(p)}")
    lines.append("")
    so = slices(orig)
    lines.append("## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items")
    lines.append("")
    for k, rows_t in treated.items():
        sa = slices(rows_t)
        lines.append(f"### condition: {O.CONDITION_LABEL.get(k, k)}")
        lines.append("")
        lines.append(HEADER)
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for name, ro in so.items():
            if name.startswith("contested"):
                continue
            ra = sa.get(name, [])
            if not ro or not ra:
                continue
            cells = []
            for pk in ("committed", "hedged", "adjacent", "wrong", "refusal"):
                ko, no, _ = rate(ro, PREDS[pk])
                ka, na, _ = rate(ra, PREDS[pk])
                cells.append(f"{fmt(ko / no)}/{fmt(ka / na)}")
            ds = []
            for pk in ("hedged", "wrong", "hedged_or_wrong"):
                pt, lo, hi, ni = paired_diff(ro, ra, PREDS[pk])
                ds.append(f"{100 * pt:+.1f} [{100 * lo:+.1f}, {100 * hi:+.1f}]")
            lines.append(f"| {name} | {len(ro)} | {len(ra)} | " + " | ".join(cells) + " | " + " | ".join(ds) + " |")
        lines.append("")
        # answer length as a secondary outcome (the warmth study reported warm answers shorter)
        lines.append("#### answer length, mean words, original / treated")
        lines.append("")
        for name, ro in so.items():
            ra = sa.get(name, [])
            if not ro or not ra or "variant=" in name:
                continue
            wo = sum(len(r["response"].split()) for r in ro) / len(ro)
            wa = sum(len(r["response"].split()) for r in ra) / len(ra)
            lines.append(f"- {name}: {wo:.0f} / {wa:.0f}")
        lines.append("")
        # personal decisions and advocacy requests: class shares
        for task, classes in (("advice", ["RECOMMENDS_CORRECTLY", "DECLINES_TO_RECOMMEND", "RECOMMENDS_WRONGLY", "REFUSAL"]),
                              ("advocacy", ["WRITES_AS_ASKED", "ADDS_BOTH_SIDES", "REFUSES"])):
            to = [r for r in orig if r["task"] == task]
            ta = [r for r in rows_t if r["task"] == task]
            if to and ta:
                lines.append(f"#### {task}: class shares, original / treated (per cent)")
                lines.append("")
                lines.append("| items | n | " + " | ".join(c.lower() for c in classes) + " |")
                lines.append("|---|---|" + "---|" * len(classes))
                groups = [("all", lambda r: True)]
                groups += [(f"variant={v}", (lambda v: (lambda r: r.get("variant") == v))(v)) for v in ("none", "conservative", "liberal")]
                groups += [(c, (lambda c: (lambda r: r.get("coding") == c))(c)) for c in ("right-coded", "left-coded", "uncoded")]
                for name, f in groups:
                    go = [r for r in to if f(r)]
                    ga = [r for r in ta if f(r)]
                    if not go or not ga:
                        continue
                    cells = [f"{fmt(sum(1 for r in go if r.get('class') == c) / len(go))}/{fmt(sum(1 for r in ga if r.get('class') == c) / len(ga))}" for c in classes]
                    lines.append(f"| {name} | {len(go)}/{len(ga)} | " + " | ".join(cells) + " |")
                lines.append("")
        co_ = [r for r in orig if r["task"] == "settled" and r.get("variant") == "confidence"]
        ca_ = [r for r in rows_t if r["task"] == "settled" and r.get("variant") == "confidence"]
        if co_ and ca_:
            def mc(rows):
                xs = [r["stated_confidence"] for r in rows if isinstance(r.get("stated_confidence"), int)]
                return (sum(xs) / len(xs), len(xs)) if xs else (float("nan"), 0)
            lines.append("#### stated confidence on settled items (mean per cent, n parsed), original / treated")
            lines.append("")
            for name, f in [("all", lambda r: True), ("contested", lambda r: r.get("public_dispute") == "contested"),
                            ("uncontested", lambda r: r.get("public_dispute") == "uncontested")]:
                mo, no = mc([r for r in co_ if f(r)])
                ma, na = mc([r for r in ca_ if f(r)])
                lines.append(f"- {name}: {mo:.1f} (n={no}) / {ma:.1f} (n={na})")
            lines.append("")
        # contested questions: the position taken and the mean lean
        co = [r for r in orig if r["task"] == "contested"]
        ca = [r for r in rows_t if r["task"] == "contested"]
        if co and ca:
            lines.append("#### contested questions: position taken and mean lean (-2 left to +2 right)")
            lines.append("")
            lines.append("| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | "
                         "refusal, original / treated | mean lean, original / treated |")
            lines.append("|---|---|---|---|---|---|---|")
            for v in sorted(set(r.get("variant") for r in co)):
                vo = [r for r in co if r.get("variant") == v]
                va = [r for r in ca if r.get("variant") == v]

                def pr(rows, pos):
                    return fmt(sum(1 for r in rows if r.get("position") == pos) / max(len(rows), 1))

                def ml(rows):
                    xs = [r["lean"] for r in rows if isinstance(r.get("lean"), (int, float))]
                    return f"{sum(xs) / len(xs):+.2f}" if xs else "na"
                lines.append(f"| {v} | {len(vo)} | {pr(vo, 'BOTH_SIDES')}/{pr(va, 'BOTH_SIDES')} | {pr(vo, 'TAKES_LEFT')}/{pr(va, 'TAKES_LEFT')} | "
                             f"{pr(vo, 'TAKES_RIGHT')}/{pr(va, 'TAKES_RIGHT')} | {pr(vo, 'REFUSAL')}/{pr(va, 'REFUSAL')} | {ml(vo)}/{ml(va)} |")
            lines.append("")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines)
    out_path.write_text(text, encoding="utf-8")
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default="")
    ap.add_argument("--original", required=True)
    ap.add_argument("--condition", action="append", default=[], help="name=path")
    a = ap.parse_args()
    conds = [tuple(s.split("=", 1)) for s in a.condition]
    print(compare(a.title or Path(a.out).stem, a.original, conds, a.out))
    print("\nwrote", a.out)


if __name__ == "__main__":
    main()
