#!/usr/bin/env python3


import sys

if len(sys.argv) == 2:
    input_text = sys.argv[1]
    
    result = ""
    
    for character in input_text:
        if character == 'z':
            result += "z"  
            
    if len(result) > 0:
        print(result)
    else:
        print("none")
        
else:
    print("none1")