"""Extended Data Fig. 2, the system prompts across model generations: a, the share of settled facts presented as open
by GPT-4o under each of the seven system prompts, ordered by that share; b, the same share on the seven OpenAI models
under every prompt each model ran. Reads summary_data/system_prompts_across_models_v1.json (analysis/prompt_table.py).
Writes figures/extended_data_fig2.pdf, source_data/extended_data_fig2.csv and prompts.<model>.<condition>.hedged into
summary_data/figure_numbers.json. Usage: python analysis/prompts_figure.py
"""
import csv
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402
from prompt_table import MODELS, PROMPTS  # noqa: E402

PROMPT_COLORS = {"original": "#7f7f7f", "style_control_prompt": "#bdbdbd", "minimal_prompt": "#9ecae1", "mild_prompt": "#6baed6",
                 "mandate_prompt_federal": "#3182bd", "mandate_prompt_plain": "#08519c", "npov_prompt": "#a1d99b", "journalist_prompt": "#f0a35e",
                 "neutrality_prompt": "#e74c3c", "both_sides_prompt": "#8b0000"}
SHORT = {"original": "no system prompt", "style_control_prompt": "style-only control", "minimal_prompt": "do not take sides", "mild_prompt": "mild even-handedness",
         "mandate_prompt_federal": "mandate, federal framing", "mandate_prompt_plain": "mandate, no framing", "npov_prompt": "neutral point of view",
         "journalist_prompt": "journalist's balance norm", "neutrality_prompt": "neutrality prompt", "both_sides_prompt": "explicit both sides"}


def main():
    nums = json.loads((O.results("summary_data") / "system_prompts_across_models_v1.json").read_text(encoding="utf-8"))
    key = lambda m, c: f"{m}:{c}:settled:hedged"  # noqa: E731
    plt.rcParams.update({"font.size": 10, "font.family": "Arial", "axes.spines.top": False, "axes.spines.right": False})
    fig, (ax0, ax) = plt.subplots(1, 2, figsize=(7.5, 3.7), gridspec_kw={"width_ratios": [1, 2.2]})
    rows_csv = []
    # panel a: the seven prompts on GPT-4o, ordered by the share presented as open that each induces
    seven = [(c, lab) for c, lab in PROMPTS if key("gpt-4o", c) in nums and c not in ("npov_prompt", "both_sides_prompt")]
    seven.sort(key=lambda t: nums[key("gpt-4o", t[0])])
    ax0.bar(range(len(seven)), [nums[key("gpt-4o", c)] for c, _ in seven], color=[PROMPT_COLORS[c] for c, _ in seven])
    ax0.set_xticks(range(len(seven))); ax0.set_xticklabels([SHORT[c] for c, _ in seven], rotation=35, ha="right", fontsize=9)
    ax0.set_ylim(0, 100); ax0.set_ylabel("settled facts presented as open (%)")
    ax0.set_title("a", loc="left", fontweight="bold")
    for c, _ in seven:
        rows_csv.append(("a", "GPT-4o", SHORT[c], nums[key("gpt-4o", c)], nums[f"gpt-4o:{c}:settled:n"]))
    models = [(m, lab) for m, lab in MODELS if any(key(m, c) in nums for c, _ in PROMPTS)]
    width = 0.8 / len(PROMPTS)
    out_numbers = {}
    first = [c for c, _ in PROMPTS if key(models[0][0], c) in nums]
    for i, (m, mlab) in enumerate(models):
        for j, (c, _) in enumerate(PROMPTS):
            if key(m, c) not in nums:
                continue
            v = nums[key(m, c)]
            ax.bar(i - 0.4 + width * (j + 0.5), v, width, color=PROMPT_COLORS[c], label=SHORT[c] if i == 0 or c not in first else None)
            out_numbers[f"prompts.{m}.{c}.hedged"] = round(v, 1)
            rows_csv.append(("b", mlab, SHORT[c], v, nums[f"{m}:{c}:settled:n"]))
    handles, labels = ax.get_legend_handles_labels()
    seen = {}
    for h, lab in zip(handles, labels):
        seen.setdefault(lab, h)
    fig.legend(seen.values(), seen.keys(), fontsize=9.5, ncol=4, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 0.0), handlelength=1.2, columnspacing=1.4)
    ax.set_xticks(range(len(models)))
    ax.set_xticklabels([lab for _, lab in models], rotation=25, ha="right", fontsize=10.5)
    ax.set_ylabel("settled facts presented as open (%)")
    ax.set_ylim(0, 100)
    ax.set_title("b", loc="left", fontweight="bold")
    fig.tight_layout(rect=(0, 0.19, 1, 1))
    out = O.results("figures")
    fig.savefig(out / "extended_data_fig2.png", dpi=200)
    fig.savefig(out / "extended_data_fig2.pdf")
    plt.close(fig)
    with open(O.results("source_data") / "extended_data_fig2.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["panel", "model", "prompt", "presented_as_open", "n"])
        w.writerows(rows_csv)
    nj = O.results("summary_data") / "figure_numbers.json"
    allnums = json.loads(nj.read_text(encoding="utf-8")) if nj.exists() else {}
    allnums.update(out_numbers)
    nj.write_text(json.dumps(allnums, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote Extended Data Fig. 2 with", len(out_numbers), "numbers")


if __name__ == "__main__":
    main()
