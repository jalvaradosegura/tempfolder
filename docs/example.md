# Example

Let's create a function that writes a file inside a folder and with the help of tempfolder, we will test it.  You won't have to take care neither of the file nor the folder, after the test execution is done.

## 📝 Create an example function that writes a file
Create a function that writes some config file into a custom folder:

``` python hl_lines="3"
def add_config_file_to_folder(folder: str):
    with open(f'{folder}/config.cfg', 'w') as f:
        f.write('I_love=tempfolder')
```

## 🗂 Import tempfolder
Import our lovely package:

``` python hl_lines="1"
from tempfolder import use_temp_folder

def add_config_file_to_folder(folder: str):
    with open(f'{folder}/config.cfg', 'w') as f:
        f.write('I_love=tempfolder')
```

## ✨ Begin to shine tempfolder! Create a test for the function

Let's create a test and use pathlib to check that things are getting created and deleted

``` python hl_lines="1 9-13"
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
```

If we test that, we get the following output:

```console
== 1 passed in 0.02s ==
```

The magic 🎩 has happened, did you missed it? Let me break it down a little bit for you:

* How did the tests passed? you didn't create the folder in which the function stores the config file...well, let me give you the answer: tempfolder
* The second assert just test that the function that we created works...
* The best for the end: If you take a look at the folder where you run the test, there is no trail of the folder nor the file 😱.

Don't take my word, let's clarify this last point with another test...

## 🕵️‍♀️ Let's double check, I don't trust you
Okey, okey...Add another test:

``` python hl_lines="18-20"
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
```

Run the test:

```console
== 2 passed in 0.03s ==
```

Told you. They are gone 🎉, thanks to tempfolder 🗂👏👏.

## 🔎 Still some doubts?

You may be thinking: hmmm but maybe the function that checks for the existence of the folder and the file runs first than the one that creates them. You can do this to check that that doesn't matter when you use tempfolder

Call the functions at the bottom of the file and run this directly with python instead of some unit test framework (like pytest ❤️):

``` python hl_lines="23-24"
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

No exception was raised right? You can even try switching the order of the function calls.

Let's see what happens if we remove our lovely tempfolder decorator:

``` python hl_lines="11"
from pathlib import Path

from tempfolder import use_temp_folder


def add_config_file_to_folder(folder: str):
    with open(f'{folder}/config.cfg', 'w') as f:
        f.write('I_love=tempfolder')


# decorator removed :(
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

Run that and we get an exception 😞, the folder doesn't exists, so it can't create the file on it:

``` console
FileNotFoundError: [Errno 2] No such file or directory: 'some_folder/config.cfg'
```

But, let's create the folder by hand and call the functions in this order:

``` console
line 18, in test_look_for_the_folder_and_the_file
    assert not Path('some_folder').exists()
AssertionError
```

With this we can check that if we don't use tempfolder the folder and the file will still exist after the execution...

If you still have doubts, take a look at your working directory, the folder and the file will be there...ugh 😖...just use tempfolder ❤️ and forget about those details.
