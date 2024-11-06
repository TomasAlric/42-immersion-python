#!/usr/bin/env python3

def add_one(x):
    x += 1
    return x

my_var = 5
print("Before calling add_one:", my_var)

my_var = add_one(my_var)

print("After calling add_one:", my_var)
