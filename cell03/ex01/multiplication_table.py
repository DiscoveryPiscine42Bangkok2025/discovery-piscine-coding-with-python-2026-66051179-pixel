#!/usr/bin/env python

try:
    print("Enter a number")
    num = int(input())
    for i in range(10):
        result = i * num
        print(str(i) + " x " + str(num) + " = " + str(result))
except ValueError:
    pass