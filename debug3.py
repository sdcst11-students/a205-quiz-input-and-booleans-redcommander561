#!python3
"""
Debug this program so that it runs

program should read a float value
and use it as an exponent rounded to 2 decimal places

original code:
x = Input("enter a float number:")
round(x)
print(x)
"""

import math

x = float(input("enter a decimal number:"))
answer = x**2
print(round(answer,2))