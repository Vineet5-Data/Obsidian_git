import os
with open('selector_agent.py') as f:
    text = f.read()

debug_inject = '''
    with open("actions_log.txt", "a") as af:
        af.write(f"Step {step} | Money: {money} | Cmd: {cmd} | Market: {market_orders}\\n")
    return {
'''
text = text.replace('    return {\n        "farmer": cmd,', debug_inject)

with open('selector_agent_debug.py', 'w') as f:
    f.write(text)

if os.path.exists('actions_log.txt'):
    os.remove('actions_log.txt')

from kaggle_environments import make
import selector_agent_debug
import v97_cap70

env = make('kaggriculture', configuration={'episodeSteps': 720, 'seed': 506952114})
env.run([selector_agent_debug.agent, v97_cap70.agent])

with open('actions_log.txt') as f:
    lines = f.readlines()
    print("".join(lines[:10]))
    print("...")
    print("".join(lines[-10:]))
