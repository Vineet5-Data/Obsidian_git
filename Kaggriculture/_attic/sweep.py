import importlib.util, itertools, sys, os
from kaggle_environments import make
def load():
    spec=importlib.util.spec_from_file_location("v2m","v2.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def run(cfg, seeds=(1000,1001,1002)):
    tot=[]
    for sd in seeds:
        m=load()
        for k,v in cfg.items(): setattr(m,k,v)
        env=make('kaggriculture',configuration={'seed':sd}); env.run([m.agent,'starter'])
        tot.append(env.steps[-1][0]['reward'])
    return tot
grid=[
 dict(WHEAT_PER_ANIMAL=6, FEED_CAP_HI=130, FEED_CAP_MID=70, FEED_CAP_LO=40),
 dict(WHEAT_PER_ANIMAL=4, FEED_CAP_HI=130, FEED_CAP_MID=70, FEED_CAP_LO=40),
 dict(WHEAT_PER_ANIMAL=4, FEED_CAP_HI=85,  FEED_CAP_MID=55, FEED_CAP_LO=38),
 dict(WHEAT_PER_ANIMAL=0, FEED_CAP_HI=85,  FEED_CAP_MID=55, FEED_CAP_LO=38),
 dict(WHEAT_PER_ANIMAL=0, FEED_CAP_HI=130, FEED_CAP_MID=70, FEED_CAP_LO=46),
 dict(WHEAT_PER_ANIMAL=2, FEED_CAP_HI=100, FEED_CAP_MID=60, FEED_CAP_LO=40),
]
for cfg in grid:
    r=run(cfg)
    print("%-70s mean=%7.0f  min=%7.0f  %s"%(cfg, sum(r)/len(r), min(r), [int(x) for x in r]), flush=True)
