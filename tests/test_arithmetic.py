"""Tests for the minimal arithmetic smoke example."""

import pytest

from mathlab.arithmetic import evaluate_polynomial


def test_evaluate_constant_polynomial() -> None:
    assert evaluate_polynomial([5.0], 100.0) == 5.0


def test_evaluate_linear_polynomial() -> None:
    assert evaluate_polynomial([3.0, -2.0], 4.0) == 10.0


def test_evaluate_higher_degree_polynomial() -> None:
    assert evaluate_polynomial([2.0, -3.0, 1.0], 2.0) == 3.0


def test_evaluate_at_negative_input() -> None:
    assert evaluate_polynomial([1.0, 0.0, -1.0], -2.0) == 3.0


def test_reject_empty_coefficients() -> None:
    with pytest.raises(ValueError, match="coefficients must not be empty"):
        evaluate_polynomial([], 1.0)
