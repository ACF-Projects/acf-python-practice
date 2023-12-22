# DICTIONARY LOOK-UP

# This line of code creates a list containing 
# a LARGE COLLECTION of valid words in the 
# English dictionary, stored in `valid_words`:
valid_words = [w.replace("\n", "").lower() for w in open("words.txt", "r").readlines()]
# Note: They are all stored in LOWERCASE!

# STEP 1: Write code that prints out how many 
# words are in the list.

print(len(valid_words))

# STEP 2: Take an input from the user.

inputword = input("Can you type a word? ")

# STEP 3: If it is a valid word, say "Valid word!". 
# For non-valid words, add them to the list of 
# valid words to add it to our dictionary.

if inputword in valid_words:
  print("Valid Word!")
else:
  print("Unknown word. Adding to dictionary...")
  valid_words.append(inputword)

# STEP 4: Take another input from the user, and 
# repeat the previous step (check if it's valid or 
# invalid). If the user types in the same invalid 
# word as before, the dictionary should now identify 
# it as a valid word.

inputword = input("Can you type another word? ")

if inputword in valid_words:
  print("Valid Word!")
else:
  print("Unknown word. Adding to dictionary...")
  valid_words.append(inputword)