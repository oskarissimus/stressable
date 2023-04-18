import stressable.utils

def test_rot13():
    assert stressable.utils.rot13('hello') == 'uryyb'

def test_rot13_empty():
    assert stressable.utils.rot13('') == ''
