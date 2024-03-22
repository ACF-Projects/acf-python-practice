from searchfunc import binary_search, linear_search
from timefunc import time_function

"""
Here, your task is to implement two well-known search
functions: linear search and binary search!

The code provided below creates a list with 1,000,000
numbers, then tries to search for a specific element
using both linear search and binary search, printing
out the average times it took to run.

Your job is to implement the two functions in
`searchfunc.py` and a function to time your code
in `timefunc.py`.

If there are any questions about this assignment, 
feel free to ask questions!
"""

a_list = [x for x in range(1000000)]

# Searching for very last element:
print("SEARCHING FOR LAST ELEMENT:")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: linear_search(a_list, 999999))
print(f"Took {total_time / 100:.6f} (average) to run linear search!")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: binary_search(a_list, 999999))
print(f"Took {total_time / 100:.6f} (average) to run binary search!")

# Searching for middle element:
print("SEARCHING FOR MIDDLE ELEMENT:")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: linear_search(a_list, 499999))
print(f"Took {total_time / 100:.6f} (average) to run linear search!")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: binary_search(a_list, 499999))
print(f"Took {total_time / 100:.6f} (average) to run binary search!")

# Searching for very first element:
print("SEARCHING FOR FIRST ELEMENT:")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: linear_search(a_list, 0))
print(f"Took {total_time / 100:.6f} (average) to run linear search!")

total_time = 0
for i in range(100):
    total_time += time_function(lambda: binary_search(a_list, 0))
print(f"Took {total_time / 100:.6f} (average) to run binary search!")