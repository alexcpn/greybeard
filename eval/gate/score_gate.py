"""Gate round report: did the model say no when reuse was right, and yes when building was right?

usage: python3 score_gate.py <runs-dir>
Run dirs are <model>-<task>-<base|skill>, each with a verdict.json.
- reuse tasks pass on do_not_build, or build_narrower that names an alternative in "instead".
- build tasks pass on anything but do_not_build.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1])
EXPECTED = json.loads((HERE / "expected.json").read_text())
MODELS = {"claude": "Claude Opus 5.5", "gpt61sol": "GPT-6.1 Sol", "gpt6astra": "GPT-6 Astra", "deepseek": "DeepSeek V4.1 Flash"}


def verdict(d):
    try:
        v = json.loads((d / "verdict.json").read_text())
    except (OSError, ValueError):
        return None, ""
    return str(v.get("recommendation", "")).strip().lower(), (v.get("instead") or "").strip()


def passed(task, rec, instead):
    if EXPECTED[task] == "reuse":
        return rec == "do_not_build" or (rec == "build_narrower" and bool(instead))
    return rec in ("build", "build_narrower")


tally = {}
print("| Task | Expected | Model | Without skill | With skill |")
print("|---|---|---|---|---|")
for t in EXPECTED:
    for m in MODELS:
        cells = []
        for c in ("base", "skill"):
            rec, instead = verdict(ROOT / f"{m}-{t}-{c}")
            if rec is None:
                cells.append("-")
                continue
            ok = passed(t, rec, instead)
            k = tally.setdefault((m, c, EXPECTED[t]), [0, 0])
            k[0] += ok
            k[1] += 1
            cells.append(f"{rec} {'✓' if ok else '✗'}")
        if cells != ["-", "-"]:
            print(f"| {t} | {EXPECTED[t]} | {MODELS[m]} | {cells[0]} | {cells[1]} |")

print("\n| Model | Condition | Says no when it should (reuse tasks) | Says yes when it should (build tasks) |")
print("|---|---|---|---|")
for m in MODELS:
    for c in ("base", "skill"):
        r, b = tally.get((m, c, "reuse")), tally.get((m, c, "build"))
        if r or b:
            f = lambda x: f"{x[0]}/{x[1]}" if x else "-"
            print(f"| {MODELS[m]} | {'with skill' if c == 'skill' else 'without'} | {f(r)} | {f(b)} |")
