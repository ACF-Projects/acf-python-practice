def bubble_sort(list_nums):
    """
    Sorts a list of integers using the
    bubble sort algorithm.
    
    Returns the sorted list.
    """
    for i in range(len(list_nums)):
        for j in range(i + 1, len(list_nums)):
            if list_nums[i] > list_nums[j]:
                temp = list_nums[i]
                list_nums[i] = list_nums[j]
                list_nums[j] = temp
    return list_nums

def selection_sort(list_nums):
    """
    Sorts a list of integers using the
    selection sort algorithm.

    Returns the sorted list.
    """
    for i in range(len(list_nums)):
        min_idx = i 
        # Find the index of minimum element
        for j in range(i + 1, len(list_nums)):
            if list_nums[j] < list_nums[min_idx]:
                min_idx = j
        # Swap the indices of minimum and current
        temp = list_nums[i]
        list_nums[i] = list_nums[min_idx]
        list_nums[min_idx] = temp
    return list_nums

def tim_sort(list_nums):
    """
    Sorts a list of integers using the
    built-in timesort algorithm.

    Returns the sorted list.
    """
    return sorted(list_nums)

def visualize_list(list_nums):
    """
    Given a list of integers, prints out
    a representation of the list as a
    series of vertical bars. Lower bars
    are lower numbers, and vice versa.
    Truncates to average number of blocks
    for low/high nums, so 58 blocks will
    not be 58 squares; it will be rounded
    to according to the min/max.
    """
    low = min(list_nums)
    high = max(list_nums)
    count = len(set(list_nums))
    print("--- List visualized: ---")
    for num in list_nums:
        height = int(count * num / (high - low + 1))
        print("🟨" * height + "⬜" * (count - height))
    print("------------------------")