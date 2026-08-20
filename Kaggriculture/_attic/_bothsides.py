"""Ground truth: replay BOTH seats verbatim at the true seed.

If this does not reproduce the recorded rewards, the fault is in extraction or
the engine version -- not in any agent.  If it DOES reproduce, then our local
v27 is not the agent that actually played, and the ladder is running a
different submission than assumed.
"""
import base64, glob, json, os, textwrap, zlib, importlib.util

TMPL = '''import base64, json, zlib
_A = json.loads(zlib.decompress(base64.b64decode((
{body}
))))
def _g(v,k,d=None):
    return v.get(k,d) if isinstance(v,dict) else getattr(v,k,d)
def agent(obs):
    try:
        s=min(max(0,int(_g(obs,"step",0) or 0)),len(_A)-1); a=_A[s] or {{}}
        fs=_g(obs,"farms",[]) or []; st=int(_g(obs,"player",0) or 0)
        n=len(_g(fs[st] if st<len(fs) else {{}}, "hands", []) or [])
        h=[list(x or ["PASS"]) for x in (a.get("hands") or [])]
        h+=[["PASS"]]*max(0,n-len(h))
        return {{"farmer":list(a.get("farmer") or ["PASS"]),"hands":h[:n],
                "market":[list(o) for o in (a.get("market") or [])][:10]}}
    except Exception:
        return {{"farmer":["PASS"],"hands":[],"market":[]}}
'''

def build(tape, path):
    blob = base64.b64encode(zlib.compress(json.dumps(tape, separators=(",", ":")).encode(), 9)).decode()
    open(path, "w", encoding="utf-8").write(
        TMPL.format(body="\n".join(f"    {l!r}" for l in textwrap.wrap(blob, 96))))

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

os.makedirs(".both", exist_ok=True)
from kaggle_environments import make
print(f"{'episode':11s}{'seed':>12s}{'recorded':>24s}{'both-verbatim replay':>26s}{'match':>7s}")
for path in sorted(glob.glob("v27_losses/*.json")):
    ep = os.path.basename(path).split(".")[0]
    rep = json.load(open(path, encoding="utf-8")); steps = rep["steps"]
    seed = rep["info"]["seed"]
    paths = []
    for seat in (0, 1):
        tape = [{"farmer": (steps[i+1][seat].get("action") or {}).get("farmer") or ["PASS"],
                 "hands": (steps[i+1][seat].get("action") or {}).get("hands") or [],
                 "market": (steps[i+1][seat].get("action") or {}).get("market") or []}
                for i in range(len(steps)-1)]
        pp = f".both/{ep}_{seat}.py"; build(tape, pp); paths.append(pp)
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed})
    env.run([load(paths[0], f"a{ep}").agent, load(paths[1], f"b{ep}").agent])
    got = [env.steps[-1][i].reward for i in (0, 1)]
    rec = [steps[-1][i].get("reward") for i in (0, 1)]
    ok = all(abs((g or 0) - (r or 0)) < 1 for g, r in zip(got, rec))
    print(f"{ep:11s}{seed:>12d}{f'{rec[0]:,.0f} / {rec[1]:,.0f}':>24s}"
          f"{f'{got[0]:,.0f} / {got[1]:,.0f}':>26s}{'YES' if ok else 'NO':>7s}")
