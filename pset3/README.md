# Problem Set 3

This file describes how to run/test PSET 3.

To run the problem set with the provided test cases, simply run:

```sh
# In the pset3/ folder
$ python pset3.py
# python.exe pset3.py on Windows
```

To test a particular function with a particular input, you can instead start a Python console (i.e., running `python` without any files) and then:
```py
>>> from pset3 import * # import all the functions in the pset3.py file
>>> isWordGuessed("secret", "attempt")
False
```

To play the demo game (once you finished the pset), you can again start a Python console and then run:
```py
>>> from pset3 import * # import all the functions in the pset3.py file
>>> play_hangman_demo()
[... game ...]
```
