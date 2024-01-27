import random
from sortfunc import bubble_sort, selection_sort, tim_sort
from timefunc import time_average

"""
Here, your task is to implement two well-known search
functions: bubble sort and selection sort!

The code provided below creates 100 randomly shuffled 
lists with 1,000 numbers each, then tries to sort each
list using both bubble sort and selection sort, printing
out the average times it took to run. It also does this
with Python's built-in sorting method called timsort.

Your job is only to implement the two functions in
`sortfunc.py`.

If there are any questions about this assignment, 
feel free to ask questions!
"""

# This code creates 100 randomly shuffled lists:
random_lists = [list(range(1000)) for x in range(100)]
for l in random_lists:
    random.shuffle(l)

time_average(bubble_sort, random_lists, "Bubble Sort")
time_average(selection_sort, random_lists, "Selection Sort")
time_average(tim_sort, random_lists, "Tim Sort")