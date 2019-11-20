

print("-app.py-")

# import arith.addition
from arith.addition import add as sum # custom-module
from random import random # core-module
from array_collections import material_array # third-party/external module

result = sum(12,13)
print(result)

arr = material_array([1,2])
new_arr = arr + 10

print(new_arr[0])
print(new_arr[1])