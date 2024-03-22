# WORD COUNTER

"""
Here, your task is to write a function that
counts the amount of times a word appears in
a given sentence.

If there are any questions about this
assignment, feel free to ask questions!
"""

# Below is a sentence. You do not need to 
# modify it in any way.
sentence = """once upon a time there was a young 
programmer learning code at a place called the 
applied computing foundation this young programmer 
was ambitious to learn python and started off in 
a program with other young and ambitious people 
like herself she learned many new things such as 
variables and loops and conditionals which she 
thought was really cool now she is a professor 
at oxford university working hard as an independent 
lifelong learner"""

# The .split() method works on any string. 
# It takes a string input (typically a single 
# character) and returns a list of the original 
# string separated by the inputted character. 
# .strip() will remove newline characters (\n)
# from the beginning/end of the string, so they
# aren't present in the list.
words = [w.strip() for w in sentence.split(" ")]

# PART 1: Print out the `words` variable to see 
# the list of words after splitting the sentence.



# PART 2: Create a function called `count`. It 
# should take a string and return the number of 
# times that word appears in the sentence. 
# (Make use of the `words` list!)
### count("and") should return 4
### count("is") should return 1
### count("programmer") should return 2



# PART 3: Find the word that appears the MOST in 
# the sentence, and print out that word. Use the 
# `count()` function to make this process easier.
### Expected: `a`, because it appears 5 times.

