#Using a program you wrote that has one function in it, 
#store that function in a separate file.
#Import the function into your main program file, 
#and call the function using each of these approaches:

'''
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

import calculator_area
print(f"Method 1 : {calculator_area.calculator(5,6)}")

from calculator_area import calculator
print(f"Method 2 : {calculator(2,4)}")

from calculator_area import calculator as calc
print(f"Method 3 : {calc(4,6)}")

import calculator_area as ca 
print(f"Method 4 : {ca.calculator(3,7)}")

from calculator_area import *
print(f"Method 5 : {calculator(2,8)}")


