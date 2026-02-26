"""
Target functions for fuzzing experiments.
"""

def my_test_function(input_str: str) -> str:
    """
    Simple crash simulation.
    Raises an exception if input equals 'crash'.
    """
    if input_str == "crash":
        raise Exception("Crash!")
    return input_str


def bc(x: str) -> int:
    """
    Branch coverage test function.
    Returns different values depending on input.
    """
    if x == "foo":
        return 1
    elif x == "bar":
        return 2
    elif x.startswith("ba"):
        return 3
    return 0