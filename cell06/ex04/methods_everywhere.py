#!/usr/bin/env python3
import sys


def shrink(my_string):
    
    print(my_string[:8])


def enlarge(my_string):
    
    missing_count = 8 - len(my_string)
   
    padding = "Z" * missing_count
    
   
    print(my_string + padding)




if len(sys.argv) < 2:
    print("none")
else:
   
    for arg in sys.argv[1:]:
        
        if len(arg) > 8:
            shrink(arg)      
            
        elif len(arg) < 8:
            enlarge(arg)      
            
        else:
            print(arg)        