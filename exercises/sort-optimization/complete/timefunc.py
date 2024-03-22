import time

def time_function(func):
  """
  Takes a function `func` and calls it.
  Returns the time (in ms) taken to call 
  the inputted function.
  """
  start_time = time.time()
  func()
  return (time.time() - start_time) * 1000

def time_average(func, random_lists, name):
  """
  Takes a function `func` and a list OF
  lists called `random_lists`. Calls `func`
  on each list INSIDE of `random_lists`.
  Prints out the average time it took
  to run, with information from the `name` 
  parameter.
  """
  total_time = 0
  for array in random_lists:
      total_time += time_function(lambda: func(array))
  print(f"{name} took {total_time / 100:.6f}ms (average) to run!")