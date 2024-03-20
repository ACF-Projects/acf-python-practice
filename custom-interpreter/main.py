from parseutil import parse_file

"""
An interpreter is a program that reads and 
executes code written in a particular 
programming language.

Here, your task is to design your own 
programming language that is executed 
through Python!

You need to implement the following:
1. `say <text>` -> prints <text>
2. `add <elem>` -> adds <elem> to database
3. `dump` -> prints all elems in database

The database is already provided below.
All commands should modify the same list.

If there are any questions about this
assignment, feel free to ask questions!
"""

database = []

def eval_line(code):
    """
    Given a list of strings `code`, 
    performs actions based on the strings
    that are passed in. (See above for more
    information on possible commands.)

    Ex: code = ["say", "hello", "world"]

    Your job is to implement this function.
    """
    # Print statement is placeholder code, 
    # but see what happens to each line of 
    # the `test.script` file!
    print(code)
 
# This line of code takes a file name and
# calls the given function on each line.
parse_file("test.script", eval_line)