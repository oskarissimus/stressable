import stressable.utils


def test_rot13():
    assert stressable.utils.rot13('hello') == 'uryyb'
    assert stressable.utils.rot13('world') == 'jbeyq'
