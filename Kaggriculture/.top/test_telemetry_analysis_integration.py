"""Tests that tournament workers retain and return observable-agent modules."""

import contextlib
import importlib.util
import io
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


HERE = Path(__file__).resolve().parent


def load_script(name):
    path = HERE / name
    spec = importlib.util.spec_from_file_location("test_" + path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class State(dict):
    def __init__(self, value, reward):
        super().__init__(value)
        self.reward = reward


class FakeEnvironment:
    def __init__(self):
        self.steps = []

    def run(self, pair):
        actions = [callable_agent({}, None) for callable_agent in pair]
        blank_farm = {
            "money": 10000.0, "tiles": [], "hands": [], "farmer": [4, 4],
            "hires_today": 0, "unlocked_quadrants": ["NW"],
        }
        observation = {
            "farms": [dict(blank_farm), dict(blank_farm)],
            "private": {"shed": {}, "seeds": {}, "inventories": [{}]},
            "market": {"prices": {}, "inventory": {}},
            "town": {"unlocked_shops": []},
        }
        for _step in range(720):
            self.steps.append([
                State({"action": actions[0], "observation": observation}, 10.0),
                State({"action": actions[1], "observation": observation}, 5.0),
            ])


AGENT_SOURCE = '''
played = 99
def reset_telemetry():
    global played
    played = 0
def agent(obs, config=None):
    global played
    played += 1
    return {"farmer": ["PASS"], "hands": [], "market": []}
def telemetry_snapshot():
    return {"schema": 1, "episodes": [], "played": played}
'''

OPPONENT_SOURCE = '''
def agent(obs, config=None):
    return {"farmer": ["PASS"], "hands": [], "market": []}
'''


class WorkerTelemetryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.agent_path = root / "a_observable.py"
        self.opp_path = root / "t_opponent.py"
        self.agent_path.write_text(AGENT_SOURCE, encoding="utf-8")
        self.opp_path.write_text(OPPONENT_SOURCE, encoding="utf-8")
        fake_kaggle = types.SimpleNamespace(make=lambda *args, **kwargs: FakeEnvironment())
        self.modules_patch = patch.dict(sys.modules, {"kaggle_environments": fake_kaggle})
        self.modules_patch.start()

    def tearDown(self):
        self.modules_patch.stop()
        self.temp.cleanup()

    def test_run_bisect_returns_same_instance_telemetry(self):
        module = load_script("run_bisect.py")
        margin, telemetry = module.one(
            (str(self.agent_path), str(self.opp_path), 7, 0))
        self.assertEqual(margin, 5.0)
        self.assertEqual(telemetry["played"], 1)

    def test_run_bisect_keeps_non_observable_agents_compatible(self):
        module = load_script("run_bisect.py")
        margin, telemetry = module.one(
            (str(self.opp_path), str(self.opp_path), 7, 1))
        self.assertEqual(margin, -5.0)
        self.assertIsNone(telemetry)

    def test_loss_analysis_embeds_same_instance_telemetry(self):
        module = load_script("_loss_analysis.py")
        result = module.one(
            (str(self.agent_path), str(self.opp_path), 7, 0, "opponent"))
        self.assertEqual(result["telemetry"]["played"], 1)

    def test_econ_analysis_embeds_same_instance_telemetry(self):
        module = load_script("_econ_loss_analysis.py")
        result = module.one(
            (str(self.agent_path), str(self.opp_path), 7, 0, "opponent"))
        self.assertEqual(result["telemetry"]["played"], 1)


class TelemetryReportTests(unittest.TestCase):
    def test_report_prints_stage_rates(self):
        module = load_script("_loss_analysis.py")
        rows = [{
            "telemetry": {"episodes": [{"days": {20: {
                "created": {"HARVEST": 10}, "admitted": {"HARVEST": 8},
                "assigned": {"HARVEST": 4}, "emitted": {"HARVEST": 3},
                "executed": {"HARVEST": 2}, "failed": {"HARVEST": 0},
                "unknown": {"HARVEST": 1}, "movement_turns": 5,
                "pass_turns": 2, "animal_cap_ticks": {"MILK": 4},
                "crop_expiry_with_yield": {},
            }}}]},
        }]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            module.report_telemetry("ALL GAMES", rows)
        rendered = output.getvalue()
        self.assertIn("HARVEST", rendered)
        self.assertIn("80.0%", rendered)
        self.assertIn("50.0%", rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
