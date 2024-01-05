from searchfunc import binary_search, linear_search
from timefunc import time_function

a_list = [x for x in range(100000)]

time_function(lambda: linear_search(a_list, 96000))