"""Elementary arithmetic utilities used to verify the learning toolchain."""

from collections.abc import Sequence


def evaluate_polynomial(coefficients: Sequence[float], x: float) -> float:
    """Evaluate a polynomial at ``x`` using Horner's method.

    Coefficients are ordered from the highest power to the constant term. For
    example, ``[2, -3, 1]`` represents ``2*x**2 - 3*x + 1``.

    Args:
        coefficients: Non-empty sequence of real polynomial coefficients.
        x: Point at which to evaluate the polynomial.

    Returns:
        The polynomial value at ``x``.

    Raises:
        ValueError: If ``coefficients`` is empty.
    """
    if not coefficients:
        raise ValueError("coefficients must not be empty")

    result = 0.0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result
