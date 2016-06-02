# Repository for Supplementary Material S2 from Medley, Goldberg and Karr: Guidelines for reproducibly building and simulating systems biology models

## Files
* `mersenne.cpp`: C++ Mersenne Twister demo which uses Boost
* `mersenne-modified.cpp`: Same as above but fully initializes internal state and reproduces Python's output
* `mersenne.py`: Python Mersenne Twister demo

## C++ / Boost instructions

* Obtain a copy of Boost 1.60.0 from www.boost.org
* Build and install the Boost random library
* Use a C++11 compiler to compile mersenne.cpp and mersenne-modified.cpp
* In the compiler command, make sure to add the Boost include path, Boost lib path, and link to both boost_random and boost_system
* Example command line:
```
clang++ -std=c++11 -I/path/to/boost-1.60.0/include -L/path/to/boost-1.60.0/lib -lboost_random -lboost_system mersenne.cpp
```

## Python instructions

* Simply run mersenne.py with a Python 2.7.10 interpreter:
```
python mersenne.py
```
