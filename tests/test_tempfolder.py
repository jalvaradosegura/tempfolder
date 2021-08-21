from pathlib import Path

from tempfolder import __version__, use_temp_folder


def test_version():
    assert __version__ == '0.1.0'


TEMP_FOLDER = Path('_temp')
FILE_PATH = TEMP_FOLDER / 'hello.txt'


def test_decorator():
    @use_temp_folder(TEMP_FOLDER)
    def write_hello():
        file_path = FILE_PATH
        with open(file_path, 'w') as f:
            f.write('hello')
            assert file_path.exists()

    write_hello()
    assert FILE_PATH.exists() is False
