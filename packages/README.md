# import

## 1. sample1: w/o __init__.py
```
>>> from greetings import hello
>>> hello.say_hello()
hello
```

## 2. sample2: w/ __init__.py
In __init__.py, define the functions of a module you want to export when the package is imported.
```
>>> import greetings2
>>> greetings2.say_hello()
hello
```

## 3. sample3: w/ subpackage
```
>>> import greetings3
>>> greetings3.say_hello()
hello
>>> import greetings3.subpackage
>>> greetings3.subpackage.say_hello()
hello
```
