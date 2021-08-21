[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/tempfolder/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/tempfolder?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![basic-quality-check](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml/badge.svg)](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml)
[![GitHub license](https://img.shields.io/github/license/jalvaradosegura/tempfolder)](https://github.com/jalvaradosegura/tempfolder/blob/main/LICENSE)

# tempfolder
🗂 Easily create temporary folders, add files into them and don't worry about deleting them, tempfolder will take care

## Installation
tempfolder is published on [PyPI](https://pypi.org/project/tempfolder/) and can be installed from there:
```
pip install tempfolder
```

## Usage
Let's see a case in which we want to test a function that creates a file inside a folder
```py
from pathlib import Path
from tempfolder import use_temp_folder


# A function that create a file inside a folder
def add_config_file_to_folder(folder: str):
    with open(Path(folder) / 'config.cfg', 'w') as f:
        f.write('i-like: tempfolder')


# Name of the temporary folder
TEMP_FOLDER = Path('temp_folder')


# Test the function
@use_temp_folder(TEMP_FOLDER)
def test_add_config_file_to_folder():
    add_config_file_to_folder(TEMP_FOLDER)
    assert TEMP_FOLDER.exists()


# Check that the temporary folder was deleted
assert not TEMP_FOLDER.exists()
```
Run with pytest:
```
========= 1 passed in 0.05s =========
```

If we remove the decorator from the previous code and run the test, we get:
```py
from pathlib import Path


# A function that create a file inside a folder
def add_config_file_to_folder(folder: str):
    with open(Path(folder) / 'config.cfg', 'w') as f:
        f.write('i-like: tempfolder')


# Name of the temporary folder
TEMP_FOLDER = Path('temp_folder')


# Test the function, now with no decorator
def test_add_config_file_to_folder():
    add_config_file_to_folder(TEMP_FOLDER)
    assert TEMP_FOLDER.exists()
```
Test:
```sh
> with open(Path(folder) / 'config.cfg', 'w') as f:
E FileNotFoundError: [Errno 2] No such file or directory: 'temp_folder/config.cfg'
```
As you can see the folder wasn't even created, because tempfolder is the one who takes care of the creation and deletion of your temporary folders (and its files).
