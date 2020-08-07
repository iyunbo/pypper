from pypper.pypper.string import strings


def test_to_str():
    assert strings.to_str("hello") == "hello"
    assert strings.to_str(b"hello") == "hello"


def test_to_bytes():
    assert strings.to_bytes("hello") == b"hello"
    assert strings.to_bytes(b"hello") == b"hello"
