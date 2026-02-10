#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
for num in array:
    if num > 5:
        new_array.append(num + 2)

print(array)
print(set(new_array))