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