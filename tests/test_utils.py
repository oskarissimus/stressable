import pytest
from stressable.utils import rot13


def test_rot13():
    assert rot13('hello') == 'uryyb'
    assert rot13('uryyb') == 'hello'
    assert rot13('!@#$%^&*()') == '!@#$%^&*()'
    assert rot13('') == ''
    assert rot13('1234567890') == '1234567890'
