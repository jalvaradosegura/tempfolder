import functools
import shutil
from pathlib import Path
from typing import Any, Callable


class TempFolderContext:
    def __init__(self, folder: str):
        self.folder = Path(folder)
        self.folder.mkdir()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        shutil.rmtree(self.folder)


def use_temp_folder(folder: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with TempFolderContext(folder):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
