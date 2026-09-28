"""Read one study's de-identified responses (responses.csv): one row per rater who finished, with the rater's
pseudonym, the attention check, three demographic items and one column per item shown (empty when not shown).
Returns a list of {"rater": id, "values": {column: value}} with numbers as integers and empty cells left out."""
import csv


def read(path):
    out = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            values = {}
            for k, v in row.items():
                if k == "rater" or v in (None, ""):
                    continue
                values[k] = int(v) if v.lstrip("-").isdigit() else v
            out.append({"rater": row["rater"], "values": values})
    return out
