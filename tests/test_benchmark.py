"""Tests for the benchmark module."""

from bosco import benchmark

from pathlib import Path
from math import isclose



def test_compute_doubling_ratio():
    """Check that the compute doubling ratio function returns the correct average doubling ratio."""
    average_doubling_ratio = benchmark.compute_average_doubling_ratio([(1, 100, 2.0000089765), (2, 200, 4.0032089765), (3, 400, 8.0076589765), (4, 800, 16.540089765)])
    assert isclose(average_doubling_ratio, 2.0224797493647424)

def test_estimate_time_complexity():
    """Ensure analyze works for various average doubling ratios."""
    assert benchmark.estimate_time_complexity(1.01) == "1"
    assert benchmark.estimate_time_complexity(1.96) == "n"
    assert benchmark.estimate_time_complexity(3.99) == "n²"
    assert benchmark.estimate_time_complexity(1.54) == "log(n)"
    assert benchmark.estimate_time_complexity(2.54) == "n log(n)"
    assert benchmark.estimate_time_complexity(100) == "not sure"
