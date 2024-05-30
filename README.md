### Air BnB Console
## About
This project is the first step in the AirBnB project for the Atlas School Higher Level Programming course. This project entails building a custom command line interpreter.

## Requirements
# Python Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ A README.md file, at the root of the folder of the project, is mandatory
+ Your code should use the pycodestyle (version 2.7.*)
+ All your files must be executable
+ The length of your files will be tested using wc
+ All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
+ All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
+ All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module"). MyClass.my_function.__doc__)')
+ A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Python UnitTests
+ Allowed editors: vi, vim, emacs
+ All your files should end with a new line
+ All your test files should be inside a folder tests
+ You have to use the unittest module
+ All your test files should be python files (extension: .py)
+ All your test files and folders should start by test_
+ Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
+ All your tests should be executed by using this command: python3 -m unittest discover tests
+ You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
+ All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
+ All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
+ All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
+ We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## The Console
The console is the command line interface which allows the user to make allowed classes, delete classes, and add attributes to those classes. This console is available in both interactive and non-interactive mode.

## How to Use the Console:
### Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


# Authors:
+ Nathan Rhys
+ Ashley Ramer