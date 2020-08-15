#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
  input()

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
    print(num + " ", end="")
