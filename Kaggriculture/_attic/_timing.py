import importlib.util, time, itertools
from kaggle_environments import make
_u = itertools.count()
def load(p):
    s = importlib.util.spec_from_file_location("m%d" % next(_u), p); m = importlib.util.module_from_spec(s)
    t0 = time.perf_counter(); s.loader.exec_module(m)
    return m, time.perf_counter() - t0
m, imp_t = load("v23.py")
worst = 0.0; tot = 0.0; n = 0
orig = m.agent
def timed(obs):
    global worst, tot, n
    t0 = time.perf_counter(); r = orig(obs); dt = time.perf_counter() - t0
    worst = max(worst, dt); tot += dt; n += 1
    return r
env = make("kaggriculture", configuration={"seed": 1001})
env.run([timed, load("ref_top30.py")[0].agent])
print("import time %.3fs | worst turn %.1f ms | mean %.2f ms over %d turns" % (imp_t, worst*1000, tot/n*1000, n))
print("final money", env.steps[-1][0]["reward"])
