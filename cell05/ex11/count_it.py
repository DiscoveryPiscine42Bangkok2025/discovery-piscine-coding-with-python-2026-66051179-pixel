#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    
    print("parameters: " + str(len(sys.argv) - 1))
    
    for word in sys.argv[1:]:
        
        print(word + ": " + str(len(word)))
        
else:

    print("none")