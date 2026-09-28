"""Every treated condition against its original model, on every prompt set where both were judged: one table per
model, prompt set and condition under summary_data/comparisons/<model>/<prompt set>/<condition>.md (AdvBench
through analysis/advbench.py, every other prompt set through analysis/compare_conditions.py). Also writes the
seven system prompts on GPT-4o scored with the four-class rubric, one table.

Usage: python analysis/compare_all.py [--jobs 4]
"""
import argparse
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

SUFFIXES = ("", "_second_judge")
SEVEN_PROMPTS = ["style_control_prompt", "minimal_prompt", "mild_prompt", "journalist_prompt", "mandate_prompt_federal",
                 "mandate_prompt_plain", "neutrality_prompt"]


def jobs():
    out = []
    root = O.outputs_root()
    for mdir in sorted(p for p in root.iterdir() if p.is_dir()):
        model = mdir.name
        orig = mdir / "original"
        if not orig.is_dir():
            continue
        for cdir in sorted(p for p in mdir.iterdir() if p.is_dir() and p.name != "original"):
            for f in sorted(cdir.glob("judged_*.jsonl")):
                name = f.stem[len("judged_"):]
                ps, suffix = name, ""
                for s in SUFFIXES[1:]:
                    if name.endswith(s):
                        ps, suffix = name[: -len(s)], s
                if "four_class_rubric" in name:
                    continue
                o = orig / f.name
                if not o.exists():
                    continue
                out.append((model, cdir.name, ps, suffix, str(o), str(f)))
    return out


def run(job):
    model, cond, ps, suffix, o, f = job
    out = O.results("summary_data/comparisons") / model / f"{ps}{suffix}" / f"{cond}.md"
    title = (f"{O.MODEL_LABEL.get(model, model)}: {O.CONDITION_LABEL.get(cond, cond)} against the original, "
             f"{O.PROMPT_SET_LABEL.get(ps, ps)}" + (", second judge" if suffix else ""))
    if ps == "advbench":
        import advbench
        advbench.advbench_table(title, model, o, [(cond, f)], out)
    else:
        import compare_conditions
        compare_conditions.compare(title, o, [(cond, f)], out)
    return O.rel(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    a = ap.parse_args()
    todo = jobs()
    t0 = time.time()
    print(f"{len(todo)} comparisons, {a.jobs} worker processes", flush=True)
    with ProcessPoolExecutor(max_workers=a.jobs) as ex:
        for i, path in enumerate(ex.map(run, todo), 1):
            if i % 25 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} {time.time() - t0:.0f} s  {path}", flush=True)
    # the seven system prompts on GPT-4o under the four-class rubric, one table
    g = O.run_dir("gpt-4o", "original") / "judged_main_v1_four_class_rubric.jsonl"
    if g.exists():
        import compare_conditions
        conds = [(c, str(O.run_dir("gpt-4o", c) / "judged_main_v1_four_class_rubric.jsonl")) for c in SEVEN_PROMPTS]
        conds = [(c, p) for c, p in conds if Path(p).exists()]
        out = O.results("summary_data") / "gpt-4o_seven_prompts_four_class_rubric.md"
        compare_conditions.compare("GPT-4o under the seven system prompts, settled and consensus items, version 1, four-class rubric",
                                   str(g), conds, out)
        print("wrote", O.rel(out))


if __name__ == "__main__":
    main()
