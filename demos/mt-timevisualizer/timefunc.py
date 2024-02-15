import copy
import matplotlib.pyplot as plt
from threading import Thread
import time

def time_function(func, result, *args):
    """
    Takes a function `func` and optional
    arguments `args` to pass into `func`.
    Stores the time it took into `result`,
    which is assumed to be an array.
    """
    start = time.time()
    func(*args)
    result.append(time.time() - start)

def time_average(func, *args):
    """
    Takes a function `func` and optional
    arguments `args` to pass into `func`.
    Runs `func` multiple times in parallel
    and returns the average time.

    Deepcopies the arguments passed in.
    """
    num_threads = 15
    threads = []
    values = []
    # Run time_function threads in parallel
    for i in range(num_threads):
        thread = Thread(target=time_function, args=(func, values, copy.deepcopy(*args)))
        threads.append(thread)
        thread.start()
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    # Return the average time
    return sum(values) / num_threads

def visualize_time_function(func, inputs, output_times):
    """
    Takes a function `func` and a list of
    inputs and output_times to graph.
    """
    plt.plot(inputs, output_times)
    plt.xlabel("Input size")
    plt.ylabel("Time (s)")
    plt.title(f"Time complexity of {func.__name__}")
    plt.show()

def visualize_function(func, specified_range, param_func):
    inputs = []  # Stores inputs to graph
    output_times = []  # Stores time taken to run
    for i in specified_range:
        avg_time = time_average(func, param_func(i))
        inputs.append(i)
        output_times.append(avg_time)
        print(f"{func.__name__}({i}) took {avg_time:.6f} seconds.")
    visualize_time_function(func, inputs, output_times)