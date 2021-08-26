# Welcome to tempfold

🗂 Easily create temporary folders, add files into them and don't worry about deleting them, tempfolder will take care.

## Installation

tempfolder is published on PyPI and can be installed from there:

``` shell
pip install tempfolder
```

## Usage

Let's see a case in which we want to test a function that creates a file inside a folder

``` python
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

```shell
========= 1 passed in 0.05s =========
```

If we remove the decorator from the previous code:

``` python
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

And then we test it:

```shell
> with open(Path(folder) / 'config.cfg', 'w') as f:
E FileNotFoundError: [Errno 2] No such file or directory: 'temp_folder/config.cfg'
```

As you can see the folder wasn't even created, because tempfolder is the one who takes care of the creation and deletion of your temporary folders (and its files).
