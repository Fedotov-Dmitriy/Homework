
import pytest 
from Walker import Walker


def test_coin_returns_only_two_values():
    w = Walker([("орел", 0.5), ("решка", 0.5)])
    for _ in range(100):
        x = w.get_random()
        assert x in ("орел", "решка")


def test_single_event_always_returned():
    w = Walker([("only", 1.0)])
    for _ in range(50):
        assert w.get_random() == "only"


def test_empty_events_raises():
    with pytest.raises(ValueError):
        Walker([])


def test_negative_probability_raises():
    with pytest.raises(ValueError):
        Walker([("a", 0.7), ("b", -0.2), ("c", 0.5)])


def test_sum_not_one_raises():
    with pytest.raises(ValueError):
        Walker([("a", 0.3), ("b", 0.3)])
