import pathlib
import sys
from os.path import isfile

import pytest

from pypper.cleancode.code_tidiness import FileTidiness
from pypper.cleancode.size import FileSize


def test_fileview_creation():
    fileview = FileTidiness(__file__)


def test_valid_file_path():
    fileview = FileTidiness(__file__)
    assert fileview.file_path == __file__
    assert isfile(fileview.file_path)


def test_get_file_size():
    fileview = FileTidiness(__file__)
    assert fileview.size


def test_get_size_in_bytes():
    fileview = FileTidiness(sample())
    assert fileview.size == FileSize(150)


def sample(filename="Sample.java"):
    dir_path = pathlib.Path(__file__).absolute()
    sample_file = str(dir_path.with_name(filename))
    return sample_file


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


def test_file_too_big_size():
    with pytest.raises(ValueError) as error:
        assert str(FileSize(sys.maxsize ** 10))
    assert caused_by_out_of_bounds(error)


def caused_by_out_of_bounds(error):
    return "file size out of bounds" in str(error.value)


def test_file_negative_size():
    with pytest.raises(ValueError) as error:
        assert str(FileSize(-1))
    caused_by_out_of_bounds(error)


def test_file_size_does_not_equal_to_other_type():
    assert FileSize(1) != 1


def test_file_code_line_count():
    fileview = FileTidiness(sample())
    assert fileview.code_lines == 7
