import random
from sortfunc import bubble_sort, selection_sort, tim_sort
from timefunc import time_function

# This code creates 100 randomly shuffled lists:
random_lists = [list(range(1000)) for x in range(100)]
for l in random_lists:
    random.shuffle(l)

total_time = 0
for array in random_lists:
    total_time += time_function(lambda: bubble_sort(array))
print(f"Took {total_time / 100:.6f}ms (on average) to run bubble sort!")

total_time = 0
for array in random_lists:
    total_time += time_function(lambda: selection_sort(array))
print(f"Took {total_time / 100:.6f}ms (on average) to run selection sort!")

total_time = 0
for array in random_lists:
    total_time += time_function(lambda: tim_sort(array))
print(f"Took {total_time / 100:.6f}ms (on average) to run tim sort!")