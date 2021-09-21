# hw-4.2.1
Simplified and lighter weight version of a command line application framework for Python.

## Usage

To create a new command line application, follow these steps:

  * In a Web broWSer:

    - Go to https://github.com/fuzzyklein/hw-4.2.1
    - Click on "Use this template".
    - Enter a name for your project and a description, if you feel like it.
    - Things will go more smoothly if the name of your project has the form:

        `name`-`version`

    - Click on "Create repository from template".
    - Clone the repository to your machine using your preferred method.
      I like SSH but I haven't tried `gh` yet.

  * In a terminal:

    - `cd <PROJECT_NAME>-<VERSION>/`
    - `sed -r --in-place=~ s/hw/<PROJECT_NAME>/ ./*/*`
    - `mv hw <PROJECT_NAME>`
    - `mv <PROJECT_NAME>/hw.py <PROJECT_NAME>/<PROJECT_NAME>.py`
    - `mv etc/hw.conf etc/<PROJECT_NAME>.conf`
    - `sed --in-place=~ s/HelloWorld/<CLASS_NAME>/ <PROJECT_NAME>/<PROJECT_NAME>.py`
    - `sed --in-place=~ s/HelloWorld/<CLASS_NAME>/ <PROJECT_NAME>/__main__.py`
    - `mv sh/hw.sh sh/<PROJECT_NAME>.sh`
    - `rm run`
    - `ln -s sh/<PROJECT_NAME>.sh run`
    - `rm */*~`
    - `./run -d`

  * `<PROJECT_NAME>` above is the name of your project and `<CLASS_NAME>` is the
    name you want to use for the class that subclasses the `Program` class.

  * If all goes well, you should see output similar to this:

    ```bash
    Program settings:
    {'all': False,
     'args': [],
     'config': None,
     'debug': True,
     'description': 'A simple and lightweight framework for a Python command line '
                    'application.',
     'follow': False,
     'input': None,
     'log': None,
     'logfile': 'log/<PROGRAM_NAME>.log',
     'output': None,
     'quiet': False,
     'recursive': False,
     'testing': False,
     'verbose': False,
     'warnings': None}

    Log file: <PROGRAM_NAME>.log

    2021-09-18 16:47:56,772 - <class '<PROGRAM_NAME>.<CLASS_NAME>> - DEBUG - Debugging <class <PROGRAM_NAME>.<CLASS_NAME>>
    Hello world
    ```

That seems to have worked pretty well so far, anyway, but this project is still in Beta.

If all goes well, then:

  * `git commit -a -m 'Update program name occurences.'; git push`

I doubt if that link works on Windoze anyway. In fact the `sh/hw.sh` script
probably only works under `PowerShell`, `WSL`, or some other `Linux` emulator
like `Cygwin` or `MSYS2`.

## Things to Do

* Write batch scripts to be used on Windoze from `Cmd`.
