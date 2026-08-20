"""Turn a recorded episode into a playable opponent.

Lets us re-fight the exact agents that beat us instead of guessing from `starter`.
The recorded side is replayed open-loop (same action every turn as in the original),
which is how the public top-30 "route" agents work anyway, so it is a fair proxy.

Usage:
    from replay_opponent import make_replay_agent, replay_seed
    opp = make_replay_agent("C:/.../90441743.json", team="yuto083")
"""
import json


def _load(path):
    with open(path) as f:
        return json.load(f)


def replay_seed(path):
    return _load(path).get("info", {}).get("seed")


def team_index(path, team_substr):
    names = _load(path)["info"]["TeamNames"]
    for i, n in enumerate(names):
        if team_substr.lower() in n.lower():
            return i
    raise ValueError("team %r not in %r" % (team_substr, names))


def make_replay_agent(path, team=None, player=None):
    """Return an agent callable that replays the recorded side's actions."""
    data = _load(path)
    p = player if player is not None else team_index(path, team)
    script = []
    for st in data["steps"]:
        a = st[p].get("action")
        script.append(a if isinstance(a, dict) else {"farmer": ["PASS"], "hands": [], "market": []})

    def agent(obs):
        step = obs.get("step", 0)
        # Kaggle stores the initial observation as steps[0]; the action applied
        # for observation step N is recorded in replay steps[N + 1].
        replay_step = step + 1
        act = script[replay_step] if replay_step < len(script) else {"farmer": ["PASS"], "hands": [], "market": []}
        # hands roster can differ by one if a HIRE was refused; trim/pad to be legal
        n_hands = len(obs["farms"][obs.get("player", 0)].get("hands") or [])
        hands = list(act.get("hands") or [])[:n_hands]
        hands += [["PASS"]] * (n_hands - len(hands))
        return {"farmer": act.get("farmer", ["PASS"]), "hands": hands,
                "market": act.get("market", [])}

    return agent
