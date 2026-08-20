"""Pool route 90635979_p0."""

import base64
import copy
import json
import math
import zlib


_ACTIONS = json.loads(zlib.decompress(base64.b64decode(
    (
    'eNrtXV1vHEly/C985oPmk6TfuNLcSTiuuKAkD84LYrHAnWHAOD+s/Wb4v1srkt09nZGRkVnVFLW6twE5012VVV2dGRkZ+fP/nv37'
    'r7/94++/nf3Lz2c/XX/4cHZ/fvYfv/7X3/778x8+f/zHr7/959//5/Pnn8/evrs7fP6v9uGHT3/95fr9ux+vb87Ozz68PRx+Ojtf'
    'm3+8vj1O/vzhcHjz+Y/Ht4frj2fnF7M//3i4uX1/dr5a39//3/nJqN+9/sunnyZXG8b/89nx8OHjl/G8v737+PbLp8dJTn43Hd7D'
    'D04n/vsgfrq7ffPp9cdxeGYYP3x6d/Pml89X//jpiw0moxhvzoYxXHj83nQc81nfXL8+PE5av5n5J7nDo+0ml55PEd7C/RK5FbHd'
    'sIKfJ/x+tP+pCR9t8bCQjfZ7us/DfvuyJ64/Hu5O7/in3/fkdFSP306Zc7zuOMmnG7y+fjTe45c6GW+c1HCn4Tt264czsGsCbGU3'
    'xOxnfJVObiBaz26I2IxP10uab9gJDeajW23YCfpWm19XtNq4E7oYCz+o8wlHVpu/k0SrTf6km83cqpO1wBx8i5h/TR6ugrGAQXwb'
    'CQ8kmYr50MlE9oNjtG7jntmq27hPPzz/ZR/PEsfBg37OxnW3hi+krmf8pscDtOka86P1a42jYF9zjSeX6g8xmcN1+8L0GMfr25ub'
    'w+uPv/zpcPfx3c27fzt9eVWu+OH2U/sy9R/Wm7vbn5Z9mj4cbn4P3SZDHiO4RTZEeAKtGq/3Yp44Zvjyzsns2143ATFtcjepGENh'
    'dTkqEEeO85WeXmZ01vXrzc+3k+uhFTAeFjTp+HA4llrdhwHKOBDg/1qfruHe1qijE2aN2nXaTfaPjZA4HHMQQWyEzK1JQFda+17T'
    'BmHLdzpvcJIsNHE3Iup077kTAKc7fHj49nK3/g5mzV/kSiy8mA3Irf+YJiiE9i/1zn2v/y1dbebfbjP+7Vb1b7mju8XZNMWzUpJi'
    'jxdTUEfmQIFbzG8vREopVzV5yzZznWSRat7+HCXtbSsUADG3cva/yi2tEe2MQE4SHrRVJ57csTDFzJuMvdbrNyQ2DSH4HrCbeL+W'
    'qHDT8aWdeJElBmTQk68whhdnFJDY/O5tAg7dfxqlV1brRQ7hm04MLnVZOVfo+cnO27+LB73ziGd9POhpgNbbh6Y8roWc6IHp0uRE'
    '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'
    'emF74wooMsEWEYOvLn3OmfmfliicGT6QfL5VUVfaAYjYXHiZYC4c40SNLKiKz/hgrvFKCDVIocYQIbhRQbGjRu2sjbGfqDpgaFUY'
    'qpb019jnzeHlWW83QKHAggBBNHwa1XrWnQg1XbUw1phyW0SM79uQL/Yqn47H8EU+EiGNz8O3WMuA5y+ymJ51YVCWKyam1A6trNau'
    'gleCd7acEle3toKkHRkEHbbuf3at9K01b2X4rGpbtjgqTd9avwiNKhLms5ZTXehZbVPZVISYj7mSA9o+SNnLfdhYEAeiqlla60Iq'
    'msZVfJt1tkgzQMb2oZWKgjT48kpbqV6LMnuH7GCn6KwsAS6raGnN1I+53uu027OSII7mu2qjmzGgNYrtJJF+YaOumzhKiS7WiO4o'
    'KXIkFdNqxDqtdoE9mKl2gXh1GSquNIVXyXQ5qS2n6ASFgI+OvdgDIrlfTRXdkHeN9ykLOaJVyTFpKhCpI90PGR0W7GTjc2hOFBgH'
    'YjJ0Gmy6iVN29SrDInQmxlBKfihpWQzyyzqd0KNg8NJbr7IpgCZr9bc6rBTtuAKlhv6pTfSLpw6ieltSv5mTNeUyYBWKzdOBJ8jF'
    'hS8rSZFfWaRSbZzyLBE+elKb7BhhzIkc1/xPPF6I0eewACHaZqe/s8tKkpGSUpthJ7V35s0lIUDheYCbWiOIbRdiulZf4f81J38N'
    '79A5kL7qgFDuv16p6CaWWij393wyUKEHouFGNVeZNrTRLLPFJMAxXUW4HE0MIIUW6MnTxJRa/hpTiAW4DXwxIZ1Y441JGyIYXKJz'
    'UsaHbgWXOZvCRK7MreyzN2jCOKB1k8hMLqBK6FpL+vCkCjTIYlKUwIVcUgNmKCjf4dTVxcs0bCZdyJdKh4Mx2/0dkoRYzyayxfVC'
    'mr1Ss3kQaWaxpOGTlZlklVhEKBTSgLkER1qibEFn0tnCBBczzO22nJ/t4RRyNzYTaKCVTcwI1dgdRMKZ2UhHlUt6iMqAesiN0wMo'
    'jkbVOegjl/Wrj3rMzBwlxL9DRyJju/Bm1nq5VViilBfJoxKKx0PcnLG5vyIaH2WHMRJbTNshiMGVoJEnQnaU6CbLo4LfFqa1L/fA'
    'DPebHDMkJeY60RFtn8Z+Qu4iUdoytgs0MjsPWZn+6EvpsZd4bdgYO9oa0GPTFZzarpmGvUMe6kycc8Ccr4dUPb+oWW9W3DepZLYK'
    'iVjflFBZeiY+mLCULJnEg6vPYxkaHCuVZBw4rgiU4Oksta0YNCq9O6l2l96jb0uO/pICGe+RSBfI8lJi6InNbaMT4FgZZhw/hrXa'
    'cqVoqO6ndo/cCmwbvi5SY1aR/SWDOmUBuUgKShAAJGvCiF5Ow4auqmOE4YZ0CkOt+7I8V+r7yitgu7nMaKx5bJpQj5IWJmMYZgTx'
    'omYPMx7qVYYhlUAi5TQN4VlJoFlNr4wVNLK3FaNvaXuRfavUERE3qhYYKjankG5EwlZZeqK2hqHHYFe7VpLCgSZEgCbqkYByj1QI'
    'zZiFiBXxouSnbzL3GUzhsyy/Q9t98kee1rbQcpceunNhAyDKTdOkbRkRqunBsWsUyP7RyQwvlPDdRS0REro2Fp61D5AlroUVqQJJ'
    'Eb4/dfEYAGxnulyqfVlsn85a1wK5oQMwhdzf0qAmM+D9sitGeGWwugvaCKEjTnj5cjodNFLzwMqtn0XNrKx+35GtBhleGVQQCrF1'
    'RggLiM1QQN+hIFYpLZVeWRe7Eizt+3XpTgVaXlQo+tptesOBAJTmmmDJGSSob0Hmne0pCgumQr6mPpwwcOQYX1A9l5AOl6uRt3sN'
    'GYKHlGWY5II/IBUTkhJzaO2uRUjmcXZ2TMMaM31trkaeXD4d32KhfSCfKJVnR2ydmuI5jfQjZZigFAIVSQ+ZZkHPz390tgIqHrXj'
    'rSFXbDWOBI9Tmlds7jMLRtnGnD0atsI9pHS1c0Q0/+kmLwRqbm0t2gQAtYxCgLXRR4ONvYIR7Dc57Y6oM+wxxQWiItipli5eM7v1'
    '5r7KI4zpjnoTXkL0TwbdAmnYrmDg7CQEzo9VKiSEKUIC1DHZRcB2PbWsp0yPznZFNtB/d1tXuMiWh0JSoT05iIhent86AVXGY5Ub'
    'APq0LIaLCjHthFI6e3UVwUmiN8K7sOCgPZ6GucTnMHiNjWv89EZdbPJRW9GeuN5m5Zl4lWxXME1fd9SY+0Pw/fIoVXM9aWeyXnKM'
    'iyJuShkVTW5lS1xdSuT+sjPjrsP4hf6E+8ruGCUp5vNhKgMZSbPnwtBYrSNVJss0TZBKR618uMMaovpxYumutKN36WKHHB+OUEAo'
    'NxM43M1bnIeP/n7XOqYqAn85+IhYk2dZ9IpKKluXzbAaYRK73cPIT8ZdRNkWb9vvah1LOXdY5LxGFY5C3H6hqKghW6LqvACJj44o'
    'Sk7J7qGjpAwewal05/DWLjXcCpk1QgTVpnBaEba27Tf3xUVAEwwwYLW6uHHjA0BULloTgU/emIGZgZO2C50sZRxRVGEDTBvmUI6i'
    'jnOI4jRcV3aZImhF1VS0tg56AwyHsHG+QAUywXbVZgISA51KyQoiZgmkFqEt7HvOyW3ANlWMbq3wk1zxfm3LRuiewYoiaFcnwgEK'
    'Gv9Nbum5159Ca6dmvQLAnUIjWzWhSnYfJ9q5sWjDYJIi9mLxVQlLaWvB0rfdbpzVqbRAJOmGhqXxRbJX+8tXzdLRRyliij2XTIuZ'
    'cAPnVgLVuRW7/LrRccqTVqW6eXJTXvOM6fFAiGuc2wVyXpWrQ2X40TpZKJBe1rtKM3GpkEFO35LSDri4LONDHAmvv4P3W+ieCCQV'
    'P2lLPPxq9/koYyhS2nm9gutwz+ONOPYDGTzahDPKpINbkKyvXZKUiI6Rh0B6sarOvJ+d9CagpaVDZ2u5TKltN4VGRNRfaiP61q9v'
    'CuJD4Z/T0d3/P/ex2jI='
    )
)))


USE_WEED = 1
# Measured OFF: the stationary idle layer lost 0-12-0 (margin -519) to the same
# agent with it disabled.  rayk's +258 on a different host does not transfer to
# this route - the extra output depresses our own premium prices.
USE_IDLE = 0
USE_IMPACT = 1

_WEED_REPLAY_STEPS = 8
_WEED_STATE = {0: {}, 1: {}}

SELLABLE_PRODUCTS = {
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
}

# base, equilibrium, scale, below shape/target, above shape/target
_MARKET_PARAMS = {
    "WHEAT": (25, 10000, 400, "sqrt", 0.8, "log", 0.2),
    "CARROT": (35, 10000, 450, "log", 0.2, "sqrt", 0.7),
    "TOMATO": (60, 10000, 200, "linear", 0.4, "sqrt", 0.6),
    "STRAWBERRY": (120, 10000, 100, "sqrt", 0.7, "linear", 1.6),
    "MELON": (250, 10000, 300, "log", 0.2, "sq", 3.6),
    "EGG": (50, 10000, 332, "linear", 0.4, "log", 0.2),
    "MILK": (160, 10000, 122, "sqrt", 0.6, "linear", 1.6),
    "WOOL": (200, 10000, 105, "log", 0.2, "sq", 3.2),
    "FERTILIZER": (100, 10000, 200, "linear", 0.4, "linear", 0.4),
}


def _get(value, key, default=None):
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _seat(obs):
    return 1 if int(_get(obs, "player", 0) or 0) == 1 else 0


def _farm(obs):
    farms = list(_get(obs, "farms", []) or [])
    seat = _seat(obs)
    return farms[seat] if seat < len(farms) else {}


def _aligned(action, obs):
    action = copy.deepcopy(action or {})
    expected = len(_get(_farm(obs), "hands", []) or [])
    hands = [list(order or ["PASS"]) for order in (action.get("hands") or [])]
    if len(hands) < expected:
        hands.extend([["PASS"] for _ in range(expected - len(hands))])
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": hands[:expected],
        "market": [list(order) for order in (action.get("market") or [])][:10],
    }


# --------------------------------------------------------------------------
# weed repair
# --------------------------------------------------------------------------
def _tile_at(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
        return (_get(farm, "tiles", []) or [])[y][x]
    except (IndexError, TypeError, ValueError):
        return "LOCKED"


def _trace_actor_action(step, actor):
    trace = _ACTIONS[min(max(int(step), 0), len(_ACTIONS) - 1)] or {}
    if actor == "farmer":
        return list(trace.get("farmer") or ["PASS"])
    hands = trace.get("hands", []) or []
    return list(hands[actor] if actor < len(hands) else ["PASS"])


def _weed_repair(obs, action, step):
    if not USE_WEED:
        return action
    action = _aligned(action, obs)
    seat = _seat(obs)
    game = _WEED_STATE[seat]
    if step == 0 or step < game.get("last_step", -1):
        game = {"last_step": step, "active": {}}
        _WEED_STATE[seat] = game
    game["last_step"] = step
    farm = _farm(obs)
    positions = [_get(farm, "farmer"), *list(_get(farm, "hands", []) or [])]
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    active = game["active"]

    for actor, transaction in list(active.items()):
        index = 0 if actor == "farmer" else int(actor) + 1
        if index >= len(units):
            active.pop(actor, None)
            continue
        age = step - transaction["start"]
        if age == 1:
            units[index] = list(transaction["intended"])
        elif 2 <= age <= 1 + _WEED_REPLAY_STEPS:
            units[index] = _trace_actor_action(step - 1, actor)
        else:
            active.pop(actor, None)

    for index, (position, intended) in enumerate(zip(positions, units)):
        actor = "farmer" if index == 0 else index - 1
        if actor in active or not isinstance(intended, list) or not intended:
            continue
        if intended[0] not in ("BUILD_PASTURE", "PLANT"):
            continue
        tile = _tile_at(farm, position)
        if not isinstance(tile, dict) or tile.get("kind") != "WEED":
            continue
        active[actor] = {"start": step, "intended": list(intended)}
        units[index] = ["DIG"]

    action["farmer"] = units[0] if units else ["PASS"]
    action["hands"] = units[1:]
    return _aligned(action, obs)


# --------------------------------------------------------------------------
# stationary idle work -- NOTHING MOVES
# --------------------------------------------------------------------------
def _idle_tile(farm, position):
    try:
        x, y = int(position[0]), int(position[1])
    except (TypeError, ValueError, IndexError):
        return None
    rows = _get(farm, "tiles", []) or []
    if not (0 <= y < len(rows) and 0 <= x < len(rows[y] or [])):
        return None
    tile = rows[y][x]
    return tile if isinstance(tile, dict) else None


def _idle_job(tile, inventory):
    """Best stationary op for this tile, or None. Fertilizer outranks the rest."""
    if tile.get("animal"):
        if tile.get("fertilizer_available"):
            return ["COLLECT_FERTILIZER"]
        if not tile.get("fed_today") and int((inventory or {}).get("WHEAT", 0) or 0) > 0:
            return ["FEED"]
        if int(tile.get("yield_units", 0) or 0) > 0:
            return ["HARVEST"]
        # The engine banks the care bonus only on a day the animal is also fed,
        # so caring an unfed animal spends the op for nothing.
        if tile.get("fed_today") and not tile.get("cared_today"):
            return ["CARE"]
        return None
    if tile.get("kind") == "PLANT" and tile.get("crop") and not tile.get("watered_today"):
        return ["WATER"]
    return None


def _idle_fill(obs, action):
    if not USE_IDLE:
        return action
    farm = _farm(obs)
    private = _get(obs, "private", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])

    def inventory_of(index):
        return inventories[index] if index < len(inventories) else {}

    def job_for(position, inventory):
        tile = _idle_tile(farm, position)
        return _idle_job(tile, inventory) if tile is not None else None

    order = action.get("farmer") or ["PASS"]
    if order and order[0] == "PASS":
        job = job_for(_get(farm, "farmer", [0, 0]), inventory_of(0))
        if job:
            action["farmer"] = job

    hands = list(action.get("hands") or [])
    positions = list(_get(farm, "hands", []) or [])
    for index, order in enumerate(hands):
        if not (order and order[0] == "PASS") or index >= len(positions):
            continue
        job = job_for(positions[index], inventory_of(index + 1))
        if job:
            hands[index] = job
    action["hands"] = hands
    return action


# --------------------------------------------------------------------------
# price-impact SELL slot ranking
# --------------------------------------------------------------------------
def _shape(name, value):
    value = max(0.0, float(value))
    if name == "linear":
        return value
    if name == "sq":
        return value * value
    if name == "sqrt":
        return math.sqrt(value)
    if name == "log":
        return math.log1p(value)
    raise ValueError(name)


def _market_price(item, inventory):
    base, equilibrium, scale, below_f, below_t, above_f, above_t = _MARKET_PARAMS[item]
    if inventory < equilibrium:
        amplitude = below_t * base / _shape(below_f, scale)
        price = base + amplitude * _shape(below_f, equilibrium - inventory)
    else:
        amplitude = above_t * base / _shape(above_f, scale)
        price = base - amplitude * _shape(above_f, inventory - equilibrium)
    return max(1, int(round(price)))


def _is_sell(order):
    return (isinstance(order, (list, tuple)) and len(order) >= 3
            and order[0] == "SELL" and order[1] in _MARKET_PARAMS)


def _impact_score(obs, order):
    if not _is_sell(order):
        return float("-inf")
    item = str(order[1])
    try:
        quantity = max(0, int(order[2]))
    except (TypeError, ValueError):
        return 0.0
    market = _get(obs, "market", {}) or {}
    inventory = _get(market, "inventory", {}) or {}
    prices = _get(market, "prices", {}) or {}
    current_inventory = int(_get(inventory, item, 10000) or 0)
    current_quote = float(_get(prices, item, _market_price(item, current_inventory)) or 0)
    later_quote = float(_market_price(item, current_inventory + quantity))
    return float(quantity) * max(0.0, current_quote - later_quote)


def _impact_slots(obs, action):
    if not USE_IMPACT:
        return action
    market = list(action.get("market") or [])
    rows = [(_impact_score(obs, order), -index, list(order))
            for index, order in enumerate(market) if _is_sell(order)]
    if len(rows) < 2:
        return action
    rows.sort(reverse=True)
    ranked = iter(row[2] for row in rows)
    action["market"] = [next(ranked) if _is_sell(o) else o for o in market]
    return action


# --------------------------------------------------------------------------
def _fix_animal_species(obs, action):
    """Keep a scripted PICKUP/PLACE legal if the two species got swapped."""
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    inventories = list(_get(private, "inventories", []) or [])
    units = [action.get("farmer", ["PASS"]), *list(action.get("hands") or [])]
    for index, unit in enumerate(units):
        if not unit or len(unit) < 2 or unit[1] not in ("COW", "SHEEP"):
            continue
        other = "SHEEP" if unit[1] == "COW" else "COW"
        if unit[0] == "PICKUP":
            if int(shed.get(unit[1], 0) or 0) <= 0 and int(shed.get(other, 0) or 0) > 0:
                unit[1] = other
        elif unit[0] == "PLACE":
            inventory = dict(inventories[index] or {}) if index < len(inventories) else {}
            if int(inventory.get(unit[1], 0) or 0) <= 0 and int(inventory.get(other, 0) or 0) > 0:
                unit[1] = other
    action["farmer"] = units[0]
    action["hands"] = units[1:]
    return action


def _terminal_liquidation(obs, action):
    if int(_get(obs, "step", 0) or 0) < len(_ACTIONS) - 1:
        return action
    private = _get(obs, "private", {}) or {}
    shed = _get(private, "shed", {}) or {}
    prices = _get(_get(obs, "market", {}) or {}, "prices", {}) or {}
    stock = [(item, max(0, int(quantity or 0)))
             for item, quantity in shed.items()
             if item in SELLABLE_PRODUCTS and int(quantity or 0) > 0]
    stock.sort(key=lambda pair: (-max(1, int(prices.get(pair[0], 1) or 1)), pair[0]))
    action["market"] = [["SELL", item, quantity] for item, quantity in stock[:10]]
    return _aligned(action, obs)


def agent(obs):
    try:
        step = min(max(0, int(_get(obs, "step", 0) or 0)), len(_ACTIONS) - 1)
        action = _aligned(_ACTIONS[step], obs)
        action = _weed_repair(obs, action, step)
        action = _fix_animal_species(obs, action)
        action = _idle_fill(obs, action)
        action = _impact_slots(obs, action)
        return _terminal_liquidation(obs, _aligned(action, obs))
    except Exception:
        return {
            "farmer": ["PASS"],
            "hands": [["PASS"] for _ in (_get(_farm(obs), "hands", []) or [])],
            "market": [],
        }
