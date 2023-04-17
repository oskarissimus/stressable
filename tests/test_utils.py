from stressable.utils import rot13


def test_rot13():
    assert rot13("test") == "grfg"
    assert rot13("grfg") == "test"
