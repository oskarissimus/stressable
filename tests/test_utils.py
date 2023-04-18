import unittest
class TestRot13(unittest.TestCase):
    def test_rot13_encodes_correctly(self):
        self.assertEqual(rot13('test'), 'grfg')