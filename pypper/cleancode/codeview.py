from pathlib import Path

from .size import FileSize


class FileView:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.size = FileSize(Path(file_path).stat().st_size)
