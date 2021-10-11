[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/tempfolder/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/tempfolder?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![basic-quality-check](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml/badge.svg)](https://github.com/jalvaradosegura/tempfolder/actions/workflows/code_quality.yml)
[![GitHub license](https://img.shields.io/github/license/jalvaradosegura/tempfolder)](https://github.com/jalvaradosegura/tempfolder/blob/main/LICENSE)

# tempfolder

🗂 Easily create temporary folders, add files into them and don't worry about deleting them, tempfolder will take care

---

Documentation: https://jalvaradosegura.github.io/tempfolder/

## Installation
tempfolder is published on [PyPI](https://pypi.org/project/tempfolder/) and can be installed from there:
```
pip install tempfolder
```

## Quick example
For a deeper explanation, please check the [docs](https://jalvaradosegura.github.io/tempfolder/)...

Run this and see if you spot the magic, if you don't, please check the [docs](https://jalvaradosegura.github.io/tempfolder/):

``` python
from pathlib import Path

from tempfolder import use_temp_folder


def add_config_file_to_folder(folder: str):
    with open(f'{folder}/config.cfg', 'w') as f:
        f.write('I_love=tempfolder')


@use_temp_folder('some_folder')
def test_add_config_file_to_folder():
    add_config_file_to_folder('some_folder')
    assert Path('some_folder').exists()
    assert Path('some_folder/config.cfg').exists()


def test_look_for_the_folder_and_the_file():
    assert not Path('some_folder').exists()
    assert not Path('some_folder/config.cfg').exists()


test_add_config_file_to_folder()
test_look_for_the_folder_and_the_file()
```
