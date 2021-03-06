import sys
from os.path import isfile

from pypper.cleancode.codeview import FileView
from pypper.cleancode.size import FileSize


def test_fileview_creation():
    fileview = FileView(__file__)


def test_valid_file_path():
    fileview = FileView(__file__)
    assert fileview.file_path == __file__
    assert isfile(fileview.file_path)


def test_get_file_size():
    fileview = FileView(__file__)
    assert fileview.size


def test_get_size_in_bytes():
    fileview = FileView("Sample.java")
    assert fileview.size == FileSize(150)


def test_file_size_human_readable_display():
    filesize = FileSize(999)
    assert str(filesize) == "999.00 Bytes"


def test_file_size_for_1_char():
    filesize = FileSize(1)
    assert str(filesize) == "1 Byte"


def test_file_size_over_1k():
    filesize = FileSize(2048)
    assert str(filesize) == "2.00 KB"


def test_file_size_0():
    filesize = FileSize(0)
    assert str(filesize) == "0 Byte"


def test_file_size_tb():
    filesize = FileSize(1458000256012)
    assert str(filesize) == "1.33 TB"


def test_file_size_undefined():
    assert str(FileSize(sys.maxsize ** 10)) == "Undefined"
    assert str(FileSize(-1)) == "Undefined"


def test_file_size_does_not_equal_to_other_type():
    assert FileSize(1) != 1
