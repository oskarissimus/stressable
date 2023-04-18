import stressable.utils

def test_rot13():
    assert stressable.utils.rot13('hello') == 'uryyb'

def test_empty_string():
    assert stressable.utils.rot13('') == ''

def test_numbers():
    assert stressable.utils.rot13('123') == '123'
