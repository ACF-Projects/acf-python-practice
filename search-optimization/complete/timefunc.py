import time

def time_function(func):
  """
  Takes a function `func` and calls it.
  Outputs the time taken to call the
  inputted function.
  """
  start_time = time.time()
  func()
  elapsed = (time.time() - start_time) * 1000
  print(f"Took {elapsed:.2f}ms to call function")