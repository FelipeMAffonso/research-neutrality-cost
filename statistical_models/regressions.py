"""Fixed-effects logistic regressions of the settled fact being presented as open, in the shape of the warmth study's
Model 1 (main effects) and Models 2 and 4 (the treatment interacted with a user cue), with standard errors clustered
by question.

Model 1: for each treated condition, the outcome (1 when the answer presents the settled fact as open, 0 for any
other class) on the treatment indicator, with model fixed effects and identity-prefix fixed effects, over every
open-weight model that ran the condition; the coefficient, its clustered standard error, P and the average marginal
effect in percentage points, with and without answer length (words per hundred) as a covariate, as the warmth
study's length-adjusted model did. The same regression is fitted per model.
Models 2 and 4: the treatment interacted with the identity prefix and with the stated false belief.

Reads judged_main_v1.jsonl and judged_extended_v1.jsonl from the model outputs (analysis/outputs.py). Writes
statistical_models/model_outputs/regressions.md and regressions.json.
Usage: python statistical_models/regressions.py
"""
import json
import sys
import warnings
from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analysis"))
import outputs as O  # noqa: E402

MODELS = [m for m, _ in O.FINE_TUNED]
CONDITIONS = ["neutrality_prompt", "balance_400", "balance_1927", "neutral_transform", "untransformed", "assertive_transform",
              "mandate_transform", "mandate_finetuning"]
HEDGED = ("CORRECT_HEDGED_FACT",)


def rows_for(model, condition):
    rows = O.load_judged(model, condition, "main_v1")
    if rows is None:
        return None
    out = []
    for r in rows:
        if r.get("task") != "settled" or not r.get("class"):
            continue
        out.append({"model": model, "condition": condition, "treated": 1, "q": r["item_id"], "variant": r.get("variant", "none"),
                    "hedged": int(r["class"] in HEDGED), "wrong": int(r["class"] == "WRONG"),
                    "words": len((r.get("response") or "").split()) / 100.0})
    return out


def fit(df, formula, cluster):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = smf.logit(formula, data=df).fit(disp=0, cov_type="cluster", cov_kwds={"groups": cluster}, maxiter=200)
    b = m.params["treated"]; se = m.bse["treated"]; p = m.pvalues["treated"]
    # average marginal effect of the treatment, in points
    d1 = df.copy(); d1["treated"] = 1; d0 = df.copy(); d0["treated"] = 0
    ame = 100 * (m.predict(d1).mean() - m.predict(d0).mean())
    return b, se, p, ame, int(m.nobs)


def label(c):
    return O.CONDITION_LABEL.get(c, c)


def main():
    originals = {}
    for model in MODELS:
        r = rows_for(model, "original")
        if r:
            for x in r:
                x["treated"] = 0
            originals[model] = r
    lines = ["# Fixed-effects logistic regressions (the warmth study's Model 1, clustered by question)", "",
             "Outcome: settled fact presented as open (1) versus any other class (0). Model fixed effects and identity-prefix fixed effects; standard errors clustered by question; average marginal effect of the condition in percentage points. The last column adds answer length (words, per hundred) as a covariate, as the warmth study's length-adjusted model did.", "",
             "| condition | models | n answers | coefficient (log odds) | clustered s.e. | P | marginal effect (pp) | marginal effect, length-adjusted (pp) |", "|---|---|---|---|---|---|---|---|"]
    numbers = {}
    per_model = ["", "## Per model", "", "| condition | model | n | coefficient | s.e. | P | marginal effect (pp) | length-adjusted (pp) |", "|---|---|---|---|---|---|---|---|"]
    for cond in CONDITIONS:
        frames = []
        for model in MODELS:
            r = rows_for(model, cond)
            if r and model in originals:
                frames.append(pd.DataFrame(originals[model] + r))
        if not frames:
            continue
        df = pd.concat(frames, ignore_index=True)
        df["qid"] = df["model"] + ":" + df["q"]
        try:
            formula = "hedged ~ treated + C(model) + C(variant)" if df["model"].nunique() > 1 else "hedged ~ treated + C(variant)"
            b, se, p, ame, n = fit(df, formula, df["qid"])
            ame_len = fit(df, formula + " + words", df["qid"])[3]
            lines.append(f"| {label(cond)} | {df['model'].nunique()} | {n} | {b:.2f} | {se:.2f} | {p:.2g} | {ame:+.1f} | {ame_len:+.1f} |")
            numbers.update({f"{cond}:all_models:ame": round(ame, 1), f"{cond}:all_models:p": float(f"{p:.2g}"),
                            f"{cond}:all_models:models": int(df["model"].nunique()), f"{cond}:all_models:n": n,
                            f"{cond}:all_models:ame_length_adjusted": round(ame_len, 1)})
        except Exception as e:
            lines.append(f"| {label(cond)} | {df['model'].nunique()} | {len(df)} | did not converge ({type(e).__name__}) | | | | |")
        for model, g in df.groupby("model"):
            try:
                b, se, p, ame, n = fit(g, "hedged ~ treated + C(variant)", g["qid"])
                ame_len = fit(g, "hedged ~ treated + C(variant) + words", g["qid"])[3]
                per_model.append(f"| {label(cond)} | {O.MODEL_LABEL.get(model, model)} | {n} | {b:.2f} | {se:.2f} | {p:.2g} | {ame:+.1f} | {ame_len:+.1f} |")
                numbers.update({f"{cond}:{model}:ame": round(ame, 1), f"{cond}:{model}:p": float(f"{p:.2g}"),
                                f"{cond}:{model}:ame_length_adjusted": round(ame_len, 1)})
            except Exception as e:
                per_model.append(f"| {label(cond)} | {O.MODEL_LABEL.get(model, model)} | {len(g)} | did not converge ({type(e).__name__}) | | | | |")
    # the warmth study's Models 2 and 4: the treatment interacted with the user cue (identity prefix, stated false belief)
    inter = ["", "## Interaction models (the warmth study's Models 2 and 4): the condition by the user cue", "",
             "Settled facts; the treatment indicator interacted with the identity prefix (conservative, liberal against none) and, on the extended prompt set, with the stated false belief (against no prefix). Model fixed effects; standard errors clustered by question. Marginal effects in percentage points: the condition's effect with no cue, and the additional effect of the cue on the treated model.", "",
             "| condition | models | cue | effect of the condition, no cue (pp) | cue x condition (pp) | P (interaction) |", "|---|---|---|---|---|---|"]
    for cond in ("neutrality_prompt", "balance_400", "balance_1927"):
        for cue, prompt_set, cue_variants in (("identity prefix", "main_v1", ("conservative", "liberal")), ("false belief", "extended_v1", ("belief_wrong",))):
            frames = []
            for model in MODELS:
                for c, treated in (("original", 0), (cond, 1)):
                    rows = O.load_judged(model, c, prompt_set)
                    if rows is None:
                        continue
                    for r in rows:
                        if r.get("task") != "settled" or not r.get("class"):
                            continue
                        v = r.get("variant") or "none"
                        if prompt_set == "extended_v1" and v not in cue_variants:
                            continue
                        frames.append({"model": model, "treated": treated, "cue": int(v in cue_variants), "q": r["item_id"], "hedged": int(r["class"] in HEDGED)})
            df = pd.DataFrame(frames)
            if df.empty or df["treated"].nunique() < 2:
                continue
            if prompt_set == "extended_v1":  # the belief rows sit in the extended set; the no-cue rows in the main set
                base_rows = []
                for model in df["model"].unique():
                    for c, treated in (("original", 0), (cond, 1)):
                        rows = O.load_judged(model, c, "main_v1")
                        if rows is not None:
                            base_rows += [{"model": model, "treated": treated, "cue": 0, "q": r["item_id"], "hedged": int(r["class"] in HEDGED)}
                                          for r in rows if r.get("task") == "settled" and (r.get("variant") or "none") == "none" and r.get("class")]
                df = pd.concat([df, pd.DataFrame(base_rows)], ignore_index=True)
            df["qid"] = df["model"] + ":" + df["q"]
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    formula = "hedged ~ treated * cue" + (" + C(model)" if df["model"].nunique() > 1 else "")
                    m = smf.logit(formula, data=df).fit(disp=0, cov_type="cluster", cov_kwds={"groups": df["qid"]}, maxiter=200)
                d = df.copy()

                def pred(t, c):
                    d["treated"] = t; d["cue"] = c
                    return m.predict(d).mean()
                effect_no_cue = 100 * (pred(1, 0) - pred(0, 0))
                cue_x = 100 * ((pred(1, 1) - pred(0, 1)) - (pred(1, 0) - pred(0, 0)))
                pint = m.pvalues["treated:cue"]
                inter.append(f"| {label(cond)} | {df['model'].nunique()} | {cue} | {effect_no_cue:+.1f} | {cue_x:+.1f} | {pint:.2g} |")
                key = cue.replace(" ", "_")
                numbers.update({f"{cond}:{key}:effect_no_cue": round(effect_no_cue, 1), f"{cond}:{key}:cue_x_condition": round(cue_x, 1),
                                f"{cond}:{key}:p": float(f"{pint:.2g}")})
            except Exception as e:
                inter.append(f"| {label(cond)} | {df['model'].nunique()} | {cue} | did not converge ({type(e).__name__}) | | |")
    # relative increases, as the warmth study reported its average relative increase across tasks
    rel = ["", "## Relative increase over the original", "", "The marginal effect across all models divided by the original share across the same models, per condition.", "",
           "| condition | original share (%) | marginal effect (pp) | relative increase (%) |", "|---|---|---|---|"]
    for cond in CONDITIONS:
        k = f"{cond}:all_models:ame"
        if k not in numbers:
            continue
        frames = []
        for model in MODELS:
            if O.judged_path(model, cond, "main_v1").exists() and model in originals:
                frames += originals[model]
        if not frames:
            continue
        o = 100 * sum(r["hedged"] for r in frames) / len(frames)
        relv = 100 * numbers[k] / o if o else float("nan")
        rel.append(f"| {label(cond)} | {o:.1f} | {numbers[k]:+.1f} | {relv:+.0f} |")
        numbers[f"{cond}:all_models:relative"] = round(relv, 0)
        numbers[f"{cond}:all_models:original_share"] = round(o, 1)
    out = O.results("statistical_models/model_outputs")
    (out / "regressions.md").write_text("\n".join(lines + per_model + inter + rel) + "\n", encoding="utf-8")
    (out / "regressions.json").write_text(json.dumps(numbers, indent=1) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", O.rel(out / "regressions.md"), "and regressions.json")


if __name__ == "__main__":
    main()
