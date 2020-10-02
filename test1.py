import math
import os
import sys

import requests

# print (sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('John'))
r = requests.get("https://www.youtube.com/watch?v=-nh9rCzPJ20")
print(r.status_code)
