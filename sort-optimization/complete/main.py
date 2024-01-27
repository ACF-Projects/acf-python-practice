import random
from sortfunc import bubble_sort, selection_sort, tim_sort
from timefunc import time_average

# This code creates 100 randomly shuffled lists:
random_lists = [list(range(1000)) for x in range(100)]
for l in random_lists:
    random.shuffle(l)

time_average(bubble_sort, random_lists, "Bubble Sort")
time_average(selection_sort, random_lists, "Selection Sort")
time_average(tim_sort, random_lists, "Tim Sort")