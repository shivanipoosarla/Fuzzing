from fuzzlab.fuzzers import afl_bitflip, afl_known_integer

def test_afl_bitflip_empty():
    assert afl_bitflip("") == ""

def test_afl_bitflip_length_preserved():
    s = "hello"
    out = afl_bitflip(s)
    assert isinstance(out, str)
    assert len(out) == len(s)

def test_afl_known_integer_appends():
    s = "x"
    out = afl_known_integer(s)
    assert out.startswith(s)
    assert len(out) >= len(s) + 1