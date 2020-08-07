from typing import Union


def to_str(bytes_or_str: Union[str, bytes]) -> str:
    """
    Ensure the type of str either from an actual str or a bytes.
    The charset to use is utf-8.
    :param bytes_or_str: an instance of a str or a bytes
    :return: the str
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str: Union[str, bytes]) -> bytes:
    """
    Ensure the type of bytes either from a str or an actual bytes.
    The charset to use is utf-8.
    :param bytes_or_str: an instance of a str or a bytes
    :return: the bytes
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value
