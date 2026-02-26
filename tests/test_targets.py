from fuzzlab.targets import bc

def test_bc_branches():
    assert bc("foo") == 1
    assert bc("bar") == 2
    assert bc("baz") == 3
    assert bc("baX") == 3
    assert bc("zzz") == 0