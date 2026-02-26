"""
Evaluation utilities for fuzzing experiments.
"""

import random
from typing import Dict

from fuzzingbook.Coverage import Coverage
from fuzzlab.targets import bc


def run_mutation_experiment(fuzzer, iterations: int = 100) -> Dict:
    """
    Run a fuzzing experiment against bc() using the provided fuzzer.

    Returns:
        Dictionary containing:
        - total_iterations
        - covered_lines
        - unique_coverage_count
    """
    cov = Coverage()

    with cov:
        for _ in range(iterations):
            fuzz_input = fuzzer.fuzz()
            bc(fuzz_input)

    coverage_data = cov.coverage()
    lines_covered = {lineno for (func, lineno) in coverage_data if func == "bc"}

    return {
        "total_iterations": iterations,
        "covered_lines": sorted(lines_covered),
        "unique_coverage_count": len(lines_covered),
    }