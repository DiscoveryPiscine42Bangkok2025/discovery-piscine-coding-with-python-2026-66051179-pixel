#!/usr/bin/env python3
import sys

if len(sys.argv) == 2                                           :
    
    target_word = sys.argv[1]
    
    user_answer = input("What was the parameter? ")
    
    if user_answer == target_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
        
else:
    print("none")