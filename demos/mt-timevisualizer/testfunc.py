import time

def bubble_sort(nums):
    """
    Sorts a list of numbers using the bubble
    sort algorithm, and then returns it.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

def my_wait_function(time_to_wait):
    """
    Waits a certain amount of seconds.
    Returns nothing.
    """
    time.sleep(time_to_wait)

def opt_sort(nums):
    """
    Sorts a list of numbers using the timsort
    algorithm, and then returns it.
    """
    nums = sorted(nums)
    return nums

def sum_nums(nums):
    """
    Sums a list of numbers and returns the result.
    """
    total = 0
    for num in nums:
        total += num
    return total