def bubble_sort(list_nums):
    """
    Sorts a list of integers using the
    bubble sort algorithm.
    
    Returns the sorted list.
    """
    pass

def selection_sort(list_nums):
    """
    Sorts a list of integers using the
    selection sort algorithm.

    Returns the sorted list.
    """
    pass

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