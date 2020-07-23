# Django File System Searcher

Django application/module that searches directories (including archives), collects file metadata and stores that metadata in a database.

Making this code work requires some [Django web framework](https://www.djangoproject.com/) skills.

## Installation

First, install the required [File System Searcher](https://github.com/thatlarrypearson/File-System-Searcher) library.

### Developer Mode Install

Developers who wish to modify the code can clone from ```github``` and install with pip.  This enables changes made in the code to appear immediately as though they were happening in the library.

```bash
python3.8 -m pip install pip --upgrade
python3.8 -m pip install setuptools --upgrade
python3.8 -m pip install wheel --upgrade
git clone https://github.com/thatlarrypearson/Django-File-System-Searcher.git
cd Django-File-System-Searcher
python3.8 setup.py build
python3.8 -m pip install -e .
```

### Library Install

If the goal is to just install and go without changes to the Django application, then follow the [Developer Mode Install](#developer-mode-install) instructions until the last step.  Replace ```python3.8 -m pip install -e .``` with ```python3.8 -m pip install --user .```.

### Check Installation

Checking the installation requires a working Django server installation.  Either follow the [Instructions For Adding To Existing Django Installation](#Instructions-For-Adding-To-Existing-Django-Installation) or [Instructions For Working With Django Server](#Instructions-For-Working-With-Django-Server).

## Instructions For Adding To Existing Django Installation

- Add "django_file_system_searcher" to INSTALLED_APPS at the end of the list:

  ```python
  INSTALLED_APPS = [
    ...
    ...
    "django_file_system_searcher",
  ]
  ```

- Include the ```django_file_system_searcher``` in the project ```urls.py``` code.

  ```python
  path('file_system_searcher/', include('file_system_searcher.urls')),
  ```

- Run ```python3.8 manage.py makemigrations file_system_searcher```

- Run ```python3.8 manage.py migrate```

- Start the development server ```python3.8 manage.py runserver``` and go to [http://127.0.0.1:8000/file_system_searcher].

- Understand the arguments to ```get_file_system``` by running the following.

  ```powershell
  > python3.8 manage.py get_file_system --help
  usage: manage.py get_file_system [-h] [--volume VOLUME] [--search_archives] [--no_hash] [--version] [-v {0,1,2,3}]
                                   [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback] [--no-color]
                                   [--force-color] [--skip-checks]
                                   [base_path [base_path ...]]

  Searches a file system and loads file information into the database

  positional arguments:
    base_path             Relative or absolute directory path where the file search begins. Default: current working
                          directory.

  optional arguments:
    -h, --help            show this help message and exit
    --volume VOLUME       Output the user provided volume name with all output records. Used to help users associate
                          external USB drives with records.
    --search_archives     Include files found in zip files in results.
    --no_hash             Do NOT generate Dropbox type hashes of files.
    --version             show program's version number and exit
    -v {0,1,2,3}, --verbosity {0,1,2,3}
                          Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
    --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided,
                          the DJANGO_SETTINGS_MODULE environment variable will be used.
    --pythonpath PYTHONPATH
                          A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
    --traceback           Raise on CommandError exceptions
    --no-color            Don't colorize the command output.
    --force-color         Force colorization of the command output.
    --skip-checks         Skip system checks.
  >
  ```

  Then to run this on a Windows 10 machine and just get pictures from the ```Pictures``` directory:

  ```powershell
  > python3.8 manage.py get_file_system --volume widebody_d --search_archives --pictures C:\Users\human\Pictures\
  ```

  It works the same way with Linux and Mac.

## Instructions For Working With Django Server

There is a repository with an example Django server setup that can be used as a starting point.

- Change directory to ```examples/django_server

- Edit ```server/settings.py``` to configure the database settings.

- Run ```python3.8 manage.py makemigrations django_file_system_searcher```

- Run ```python3.8 manage.py migrate```

- Run ```python 3.8 manage.py migrate createsuperuser```

- Follow the [Instructions For Adding To Existing Django Installation](#Instructions-For-Adding-To-Existing-Django-Installation) that haven't been done yet.
