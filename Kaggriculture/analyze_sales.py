import json
import sys

def main():
    try:
        with open('replay.json') as f:
            replay = json.load(f)
    except FileNotFoundError:
        print("No replay.json found. Run play_one.py first to generate it.")
        return
        
    steps = replay['steps']
    
    # We want to track sales of STRAWBERRY by both players and the price at that step
    p0_strawberry_sales = []
    p1_strawberry_sales = []
    
    for step_idx, step_data in enumerate(steps):
        if step_idx == 0:
            continue
            
        # The actions taken in the PREVIOUS step are recorded in this step's agent state?
        # Actually, let's just look at the money delta and inventory delta.
        # But we can also look at the market prices.
        obs = step_data[0]['observation']
        prices = obs['market']['prices']
        st_price = prices.get('STRAWBERRY', 0)
        
        # Look at actions taken in the previous step
        for player_idx, agent_state in enumerate(step_data):
            action = agent_state.get('action')
            if not action:
                continue
                
            # action is a dict like {'market': [['SELL', 'STRAWBERRY', 5], ...], 'farmer': ...}
            market_actions = action.get('market', [])
            for m_action in market_actions:
                if len(m_action) >= 3 and m_action[0] == 'SELL' and m_action[1] == 'STRAWBERRY':
                    qty = m_action[2]
                    print(f"Step {step_idx} (Day {step_idx//24}, Hour {step_idx%24}): Player {player_idx} sells {qty} STRAWBERRY at price {st_price}")
                    if player_idx == 0:
                        p0_strawberry_sales.append((step_idx, qty, st_price))
                    else:
                        p1_strawberry_sales.append((step_idx, qty, st_price))
                        
    print(f"\nTotal STRAWBERRY sold by P0: {sum(q for _, q, _ in p0_strawberry_sales)}")
    print(f"Total STRAWBERRY sold by P1: {sum(q for _, q, _ in p1_strawberry_sales)}")
    
if __name__ == "__main__":
    main()
