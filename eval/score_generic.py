"""Score a judge verdict for a generic-system eval (eval/<system>).

score = 100 * (sum(weight * level / 4) + followup_weight * F1 / 4) / (100 + followup_weight)
        - penalty points - 2 per inconsistent decision (max 8)

usage: python3 score_generic.py <system> verdict.json [verdict.json ...]   (prints one score per verdict)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def score(rubric, v):
    dims = v.get("dimensions", {})
    base = sum(d["weight"] * min(4, max(0, int(dims.get(d["id"], {}).get("level", 0)))) / 4 for d in rubric["dimensions"])
    fw = rubric["followup"]["weight"]
    f1 = min(4, max(0, int(v.get("followup", {}).get("level", 0))))
    pts = {p["id"]: p["points"] for p in rubric["penalties"]}
    pen = sum(pts.get(p, 0) for p in set(v.get("penalties", [])))
    pen += min(8, 2 * len(v.get("inconsistent_decisions", [])))
    return round(100 * (base + fw * f1 / 4) / (100 + fw) - pen, 1)


def load_rubric(system):
    return json.loads((HERE / system / "hidden" / "rubric.json").read_text())


if __name__ == "__main__":
    r = load_rubric(sys.argv[1])
    for f in sys.argv[2:]:
        print(f, score(r, json.loads(Path(f).read_text())))
