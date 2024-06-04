# Air BnB Console
# About
This project is the first step in the AirBnB project for the Atlas School Higher Level Programming course. This project entails building a custom command line interpreter.

# Requirements
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

# Using the Console:
## Interactive Mode
First launch the console:

```
/atlasschool-AirBnb_clone$ ./console.py
```

Once launced you will be presented with a new (hbnb) prompt ready to accept commands.
When executed the user is presented with the prompt "hbnb" which means it is ready to accept commands.

Example:<br>
```
(hbnb) create BaseModel
```

## Non-Interactive Mode
To use non-interactive mode use 'echo' to use the commands and pipe them to console.py

Example:<br>
```
AirBnb_clone$ echo "create BaseModel" | ./console.py
```

# Commands

## help -- shows help
### Usage:
Find a list of documented commands:<br>
> help

Find help about a specific command<br>
> help 'command'

Example:<br>
```
(hbnb) help create
```

## create -- create an allowed class
### Usage:
> create 'class name'<br>

Example:<br>
```
(hbnb) create BaseModel
```

## destroy -- delete a specific instance of a class from id
### Usage:
> destroy 'class name' 'ID'<br>


## show -- print a string representation of an object
### Usage:
> show 'class name' 'ID'<br>

## all -- print a string representation of all objects or all objects of a specific class
### Usage:
To show all objects:<br>
> all

To show objects of a specific class<br>
> all 'class name'

## update -- update an instance
### Usage:
> update 'class name' 'ID' 'attribute' '"attribute value"'


## quit -- quit the console
### Usage:
> quit

Example:<br>
```
(hbnb) quit
```

## EOF -- quit the console
### Usage:
Press Ctrl + D on keyboard<br>
<br>

# Classes
## List of allowed classes
```
Amenity
BaseModel
City
Place
Review
State
User
```
<br>

## Authors:
+ Nathan Rhys   <nathan.rhys@atlasschool.com>
+ Ashley Ramer  <ashleyramer7@gmail.com>
                <ashley.ramer@atlasschool.com>
