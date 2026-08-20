"""Local ablation: extra care/water workers plus adaptive premium liquidation."""

import candidate_route_market as market_policy
import candidate_route_workers as worker_policy


def agent(obs):
    action = worker_policy.agent(obs)
    step = min(
        max(0, int(worker_policy._get(obs, "step", 0) or 0)),
        len(worker_policy._ACTIONS) - 1,
    )
    return market_policy._adaptive_market(obs, action, step)
