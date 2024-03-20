import os
from parseutil import parse_file

database = []

def eval_line(code):
    """
    Given a list of strings `code`, 
    performs actions based on the strings
    that are passed in. (See above for more
    information on possible commands.)
    """
    # First, we create `command` (first
    # keyword provided) and `message` (all
    # following keywords)
    command = code[0]
    message = ""
    for i in range(1, len(code)):
        message += code[i]
        if i != len(code):
            message += " "
    # Then perform actions based on `command`
    if command == "say":
        print(message)
    elif command == "add":
        database.append(message)
    elif command == "dump":
        print("-- DATA DUMP --")
        for data in database:
            print(data)
        print("-- DATA END --")
 
# This line of code takes a file name and
# calls the given function on each line.
parse_file(os.path.dirname(__file__) + "/../test.script", eval_line)