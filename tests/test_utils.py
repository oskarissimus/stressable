import codecs
def test_rot13():
    assert codecs.encode('test', 'rot13') == 'grfg'
