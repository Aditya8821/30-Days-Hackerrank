import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip=(tip_percent/100)*meal_cost
    tax=(tax_percent/100)*meal_cost
    print(round(tip+tax+meal_cost))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
