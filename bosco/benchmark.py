"""Conduct doubling experiments for provided algorithms that perform list sorting."""

import os
import sys
from timeit import repeat
from typing import List, Tuple


def run_sorting_algorithm(
    file_path: str, algorithm: str, array: List[int]
) -> Tuple[float, float, float]:
    """Run a sorting algorithm and profile it with the timeit package."""
    directory, file_name = os.path.split(file_path)
    module_name = os.path.splitext(file_name)[0]

    if directory:
        sys.path.append(directory)

    try:
        module = __import__(module_name)
        algorithm_func = getattr(module, algorithm)
    except (ImportError, AttributeError):
        raise ValueError(f"Could not import {algorithm} from {file_path}")

    stmt = f"{algorithm_func.__name__}({array})"
    times = repeat(
        setup=f"from {module_name} import {algorithm}",
        stmt=stmt,
        repeat=3,
        number=10,
    )
    return min(times), max(times), sum(times) / len(times)


def compute_average_doubling_ratio(times_list: List[Tuple[float, float, float]]) -> float:
    """Calculate the doubling ratios."""
    times = [item[2] for item in times_list]
    # iterate through times, calculating doubling ratios between runs
    doubling_ratios = [times[i+1] / times[i] for i in range(len(times) - 1)]
    # calculate average doubling ratio
    return sum(doubling_ratios) / len(doubling_ratios)

def estimate_time_complexity(average_doubling_ratio: float) -> str:
    """Estimate the time complexity given the average doubling ratio."""
    average_doubling_ratio_rounded = round(average_doubling_ratio)
    if average_doubling_ratio >= 1.75 and average_doubling_ratio <= 2.25:
        return "n"
    elif average_doubling_ratio > 2.25 and average_doubling_ratio < 3.75:
        return "n log(n)"
    elif average_doubling_ratio >= 3.75 and average_doubling_ratio_rounded <= 4.25:
        return "n²"
    elif average_doubling_ratio > 1.25 and average_doubling_ratio < 1.75:
        return "log(n)"
    elif average_doubling_ratio_rounded == 1:
        return "1"
    # indicate that it does not match any of our predefined values
    else:
        return "not sure"
