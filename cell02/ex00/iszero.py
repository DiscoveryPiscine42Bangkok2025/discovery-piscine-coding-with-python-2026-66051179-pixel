#!/usr/bin/env python

try:
    num = int(input())
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("This number is different from zero.")
    