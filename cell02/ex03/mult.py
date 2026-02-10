#!/usr/bin/env python
try:
    print("Enter the first number:")
    num1 = int(input())
    
    print("Enter the second number:")
    num2 = int(input())
    
    result = num1 * num2
    
    print(str(num1) + " x " + str(num2) + " = " + str(result))
    
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")
except ValueError:
    pass