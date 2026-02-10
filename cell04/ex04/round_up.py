#!/usr/bin/env python
import math  

try:
    user_input = input("Give me a number: ")
    num = float(user_input)
    
    # ปัดเศษขึ้นเป็นจำนวนเต็ม
    result = math.ceil(num)
    
    print(result)
    
except ValueError:
    print("Error: That's not a number.")
