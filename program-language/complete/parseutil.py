def parse_file(file_name, func):
    """
    This code opens up a file and calls
    the `func()` function on every 
    parsed line in the file, splitting
    keywords by space characters (" ").

    If the file name is invalid, throws
    an error.

    You do not need to modify this code.
    """
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip()
            func(words.split(" "))