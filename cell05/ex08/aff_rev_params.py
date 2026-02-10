#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:

    params = sys.argv[1:]
    
    params.reverse()
    
    for x in params:
        print(x)
else:
    print("none")