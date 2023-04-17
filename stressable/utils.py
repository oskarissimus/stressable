import codecs


def rot13(s: str) -> str:
    """Rot13 a string"""
    return codecs.encode(s, "rot13")
