from pathlib import Path

from .size import FileSize


class FileTidiness:
    def __init__(self, file_path: str):
        self.file_path = file_path
        stat = Path(file_path).stat()
        self.size = FileSize(stat.st_size)
        self.code_lines = FileTidiness.count_lines(file_path)

    @staticmethod
    def count_lines(file_path):
        with open(file_path) as f:
            lines, empty_lines = FileTidiness.count_code_lines(f)
        return lines - empty_lines

    @staticmethod
    def count_code_lines(f):
        empty_lines = 0
        line_counter = 0

        for line_counter, line in enumerate(f):
            if not line.strip():
                empty_lines += 1

        return line_counter + 1, empty_lines
