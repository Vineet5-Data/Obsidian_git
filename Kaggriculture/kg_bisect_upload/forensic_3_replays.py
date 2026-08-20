import json
from kaggle_environments import make

REPLAYS = [
    ("Replay 93087343", r"C:\Users\Vinee\Downloads\93087343.json", 0),
    ("Replay 93088274", r"C:\Users\Vinee\Downloads\93088274.json", 0),
    ("Replay 93089211", r"C:\Users\Vinee\Downloads\93089211.json", 1),
]

for name, path, our_seat in REPLAYS:
    opp_seat = 1 - our_seat
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"\n=======================================================")
    print(f"DEEP DIVE: {name}")
    print(f"=======================================================")
    
    # Analyze where the opponent gained coins turn by turn
    opp_income_by_item = {}
    our_income_by_item = {}
    
    # We can inspect the market prices and sales in the steps
    for step_idx in range(len(data["steps"]) - 1):
        step_now = data["steps"][step_idx]
        step_next = data["steps"][step_idx + 1]
        
        # Check sales
        act_our = step_now[our_seat].get("action")
        act_opp = step_now[opp_seat].get("action")
        
        # Check cash change
        m_our_before = step_now[our_seat]["observation"]["farms"][our_seat]["money"]
        m_our_after = step_next[our_seat]["observation"]["farms"][our_seat]["money"]
        
        m_opp_before = step_now[opp_seat]["observation"]["farms"][opp_seat]["money"]
        m_opp_after = step_next[opp_seat]["observation"]["farms"][opp_seat]["money"]
        
        if isinstance(act_our, dict):
            for m in act_our.get("market", []):
                if m and m[0] == "SELL":
                    item, qty = m[1], int(m[2] or 0)
                    our_income_by_item[item] = our_income_by_item.get(item, 0) + qty
                    
        if isinstance(act_opp, dict):
            for m in act_opp.get("market", []):
                if m and m[0] == "SELL":
                    item, qty = m[1], int(m[2] or 0)
                    opp_income_by_item[item] = opp_income_by_item.get(item, 0) + qty
                    
    print("Units Sold Comparison:")
    all_items = set(list(opp_income_by_item.keys()) + list(our_income_by_item.keys()))
    for item in sorted(all_items):
        q_our = our_income_by_item.get(item, 0)
        q_opp = opp_income_by_item.get(item, 0)
        print(f"  {item:<12}: v142={q_our:<5} | Opponent={q_opp:<5} | Diff: {q_our - q_opp:+5}")
