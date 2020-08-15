#!/bin/python3

import math
import os
import random
import re
import sys


def  slove(meal_cost, tip_percent, tax_percent):
     tax = meal_cost * (tax_percent / 100)
     tip = meal_cost * (tip_percent / 100)
     total_cost = meal_cost + tip + tax
     roundedvalue = round(total_cost)
     print(roundedvalue)


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())
   
    tax_percent = int(input().strip())
   
    solve(meal_cost, tip_percent, tax_percent) 
