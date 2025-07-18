# Problem Set 4

This file describes how to run/test PSET 4.

To run the first part of the problem set with the provided test cases, simply run:

```sh
# In the pset4/ folder
$ python pset4_game.py
# python.exe pset4_game.py on Windows
```

If all the tests pass, this will then open the game itself (human-human mode).

To test a particular function with a particular input, you can instead start a Python console (i.e., running `python` without any files) and then:
```py
>>> from pset4_game import * # import all the functions in the pset4_game.py file
>>> getWordScore("weed", 4)
32
```

To play against the computer (once you've done that part) you can run the same thing with `python pset4_skynet.py`.
```
