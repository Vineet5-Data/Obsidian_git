"""Where is the money actually lost?  Realized $/unit per item, us vs Seb."""
import collections, importlib.util, sys
from kaggle_environments import make

def L(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

v = L('v27.py', 'v')
mine = sys.argv[1] if len(sys.argv) > 1 else 'v27.py'
opp = sys.argv[2] if len(sys.argv) > 2 else '.field/f_90639963_p1.py'
env = make('kaggriculture', configuration={'episodeSteps': 720, 'seed': 12345})
env.run([L(mine, 'a').agent, L(opp, 'b').agent])

rev = [collections.Counter(), collections.Counter()]
qty = [collections.Counter(), collections.Counter()]
ph  = [collections.Counter(), collections.Counter()]
for i in range(len(env.steps) - 1):
    inv = dict(env.steps[i][0]['observation']['market']['inventory'])
    for s in (0, 1):
        act = env.steps[i + 1][s].get('action') or {}
        for o in (act.get('market') or []):
            if o and o[0] == 'SELL' and len(o) >= 3:
                item, n = o[1], int(o[2])
                rev[s][item] += sum(v._market_price(item, inv[item] + k) for k in range(n))
                qty[s][item] += n
                ph[s][i % 4] += n

print('%-11s %8s %9s %8s | %8s %9s %8s' % ('item', 'qty', 'revenue', '$/unit', 'qty', 'revenue', '$/unit'))
for item in ('MILK', 'STRAWBERRY', 'WOOL', 'MELON', 'WHEAT', 'FERTILIZER'):
    q0, r0, q1, r1 = qty[0][item], rev[0][item], qty[1][item], rev[1][item]
    print('%-11s %8d %9.0f %8.1f | %8d %9.0f %8.1f'
          % (item, q0, r0, r0 / max(1, q0), q1, r1, r1 / max(1, q1)))
print('\ntotal revenue   mine %.0f   opp %.0f' % (sum(rev[0].values()), sum(rev[1].values())))
print('units by step%%4  mine %s   opp %s' % (dict(sorted(ph[0].items())), dict(sorted(ph[1].items()))))
print('final reward', env.steps[-1][0].reward, env.steps[-1][1].reward)
