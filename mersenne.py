import random

random.seed(100)
print("First five pseudo-random numbers generated" +
      "by Python's random module:")
print("{}, {}, {}, {}, {}".format(
  random.getrandbits(32), random.getrandbits(32), random.getrandbits(32),
  random.getrandbits(32), random.getrandbits(32)))