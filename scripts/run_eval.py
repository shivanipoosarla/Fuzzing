"""
CLI runner for fuzzing evaluation.

Run:
  PowerShell:
    $env:PYTHONPATH="src"
    py scripts/run_eval.py --iterations 200 --seed 0
"""

import argparse
import random

from fuzzlab.fuzzers import CustomMutationFuzzer
from fuzzlab.evaluation import run_mutation_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run fuzzing coverage evaluation.")
    parser.add_argument("--iterations", type=int, default=200, help="Number of fuzzing iterations")
    parser.add_argument("--seed", type=int, default=0, help="Random seed for reproducibility")
    args = parser.parse_args()

    random.seed(args.seed)

    seeds = ["foo", "bar", "baz"]
    fuzzer = CustomMutationFuzzer(seeds)

    result = run_mutation_experiment(fuzzer, iterations=args.iterations)

    print("=== Fuzzing Evaluation Summary ===")
    print(f"Iterations: {result['total_iterations']}")
    print(f"Unique bc() lines covered: {result['unique_coverage_count']}")
    print(f"Covered lines: {result['covered_lines']}")
    print(f"Seed: {args.seed}")


if __name__ == "__main__":
    main()