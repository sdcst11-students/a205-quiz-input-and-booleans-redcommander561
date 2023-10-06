"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

value1 = float(input("Enter the first number: "))
value2 = float(input("Enter the second number: "))

hypotenuese = str(input("is one of the numbers the hypotenuese? "))

if hypotenuese =="yes":
    answer = (value1**2 - value2**2)**0.5
    print(round(answer,1))
elif hypotenuese =="no":
    value1 >= value2
    answer = value2 / math.sqrt(2)
    
    print(round(answer,1))

elif hypoteneuse =="no" and value2 >= value1:
    answer = value1 / math.sqrt(2)
    print(answer)

exit()
 
