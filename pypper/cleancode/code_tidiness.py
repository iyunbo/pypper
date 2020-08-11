from pathlib import Path

from .size import FileSize


class FileTidiness:
    def __init__(self, file_path: str):
        self.file_path = file_path
        stat = Path(file_path).stat()
        self.size = FileSize(stat.st_size)
