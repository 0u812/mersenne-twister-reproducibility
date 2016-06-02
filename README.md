# Repository for Supplementary Material S2 from Medley, Goldberg and Karr

## C++ / Boost instructions

* Obtain a copy of Boost 1.60.0 from www.boost.org
* Build and install the Boost random library
* Use a C++11 compiler to compile mersenne.cpp and mersenne-modified.cpp
* Example command line:
```
clang++ -std=c++11 -I/path/to/boost-1.60.0/include -L/path/to/boost-1.60.0/lib -lboost_random -lboost_system mersenne.cpp
```

## Python instructions

* Simply run mersenne.py with a Python 2.7.10 interpreter:
```
python mersenne.py
```
