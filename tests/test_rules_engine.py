import pytest

from src.rules_engine import RulesEngine

@pytest.fixture
def rules_engine():
    engine = RulesEngine()
    return engine

@pytest.mark.parametrize("rule, input_data, expected_result", [
    ('a == 10',{'a':10},True),
    ('a == 10',{'a':11},False),
    ('a > 10',{'a':11},True),
    ('a > 10',{'a':10},False),
])
def test_simple_numeric_conditions(rules_engine, rule, input_data, expected_result):
    actual = rules_engine.evaluate_rule(rule, input_data)
    assert actual == expected_result

