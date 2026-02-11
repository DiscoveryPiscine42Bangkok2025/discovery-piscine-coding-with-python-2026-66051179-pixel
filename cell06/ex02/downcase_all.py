#!/usr/bin/env python3
import sys


def downcase_it(my_string):
    return my_string.lower()

if len(sys.argv) > 1:
    
    for param in sys.argv[1:]:
        
        print(downcase_it(param))
        
else:
    print("none")