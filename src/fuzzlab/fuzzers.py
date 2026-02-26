"""
Fuzzers and mutation strategies used in this project.
"""

import random
import string
from typing import List

from fuzzingbook.Fuzzer import RandomFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer


class MyRandomFuzzer(RandomFuzzer):
    """
    Custom random fuzzer (currently uses default RandomFuzzer behavior).
    """
    def fuzz(self) -> str:
        return super().fuzz()


class CustomMutationFuzzer(MutationFuzzer):
    """
    Mutation fuzzer overriding mutate() with a simple character replacement.
    """
    def mutate(self, inp: str) -> str:
        if len(inp) > 0:
            i = random.randrange(len(inp))
            return inp[:i] + random.choice(string.printable) + inp[i + 1:]
        return random.choice(string.printable)


def afl_bitflip(data: str) -> str:
    """
    Flip the least significant bit of a random character.
    """
    if len(data) == 0:
        return data

    i = random.randrange(len(data))
    b = ord(data[i])
    b ^= 0x01
    return data[:i] + chr(b) + data[i + 1:]


def afl_known_integer(data: str) -> str:
    """
    Append a known "interesting" integer value.
    """
    known_ints = ["0", "1", "255", "32767", "2147483647"]
    return data + random.choice(known_ints)