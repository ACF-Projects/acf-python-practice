def linear_search(my_list, target_elem):
  """
  Performs a linear search on `my_list`
  by looking for elements from front to
  back until `target_elem` is found.

  Assumes that `target_elem` is sorted.

  Returns the element's index if found,
  or else returns -1.
  """
  for i in range(len(my_list)):
      if my_list[i] == target_elem:
          return i
  return -1

def binary_search(my_list, target_elem):
  """
  Performs a binary search on `my_list`
  by starting at the half point of the
  list and cutting off the half that
  does not contain the element until 
  `target_elem` is found.

  Assumes that `target_elem` is sorted.

  Returns the element's index if found,
  or else returns -1.
  """
  low = 0
  high = len(my_list) - 1
  while low <= high:
      mid = (low + high) // 2
      curr = my_list[mid]
      if curr == target_elem:
          return mid
      elif curr < target_elem:
          low = mid + 1
      else:
          high = mid - 1
  return -1