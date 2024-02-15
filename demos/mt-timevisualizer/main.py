from testfunc import bubble_sort, my_wait_function, opt_sort, sum_nums
from timefunc import visualize_function

visualize_function(bubble_sort, range(0, 1500, 100), lambda i: [j for j in range(i, 0, -1)])

visualize_function(my_wait_function, range(0, 10, 1), lambda i: 0.1)

visualize_function(opt_sort, range(0, 1500000, 200000), lambda i: [j for j in range(i, 0, -1)])

visualize_function(sum_nums, range(0, 500000, 100000), lambda i: [j for j in range(i)])