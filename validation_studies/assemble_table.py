"""The human validation table, assembled from the three studies' outputs in the order the paper reports them: the rater
study, the pair study and the face-validity study. Writes summary_data/human_validation.md.
Usage: python validation_studies/assemble_table.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analysis"))
import outputs as O  # noqa: E402

PARTS = ["validation_rater_study.md", "validation_pair_study.md", "validation_face_validity_study.md"]


def main():
    out = O.results("summary_data")
    chunks, missing = [], []
    for name in PARTS:
        p = out / name
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8").strip())
        else:
            missing.append(name)
    (out / "human_validation.md").write_text("\n\n".join(chunks) + "\n", encoding="utf-8")
    print("assembled", len(chunks), "part(s);", "missing: " + ", ".join(missing) if missing else "all parts present")


if __name__ == "__main__":
    main()
