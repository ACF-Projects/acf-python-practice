# DICTIONARY LOOK-UP

"""
Here, your task is to validate words that the
user types in to see if they're real words in
the English dictionary.

To do this, we provide a `valid_words` list below
that contains a ton of valid words in the English
dictionary.

If there are any questions about this
assignment, feel free to ask questions!
"""

# This line of code creates a list containing a
# LARGE COLLECTION of words in the dictionary.
# (Note: They're all in lowercase!)
valid_words = [w.replace("\n", "").lower() for w in open("words.txt", "r").readlines()]

# STEP 1: Write code that prints out how many 
# words are in the list.



# STEP 2: Take an input from the user.



# STEP 3: Tell the user if ther word IS or IS NOT
# a valid word in the English dictionary. For non-valid 
# words, add it to our list of valid words to recognize 
# them later on.



# STEP 4: Take another input from the user, and 
# repeat the previous step (check if it's valid or 
# invalid). If the user types in the same invalid 
# word as before, the dictionary should now identify 
# it as a valid word.

