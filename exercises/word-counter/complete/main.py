# WORD COUNTER

# Below is a sentence. You do not need to 
# modify it in any way.
sentence = "once upon a time there was a young programmer learning code at a place called the applied computing foundation this young programmer was ambitious to learn python and started off in a program with other young and ambitious people like herself she learned many new things such as variables and loops and conditionals which she thought was really cool now she is a professor at oxford university working hard as an independent lifelong learner"

# The .split() method works on any string. 
# It takes a string input (typically a single 
# character) and creates a list of the original 
# string separated by the inputted character. 
# You do not need to modify this line in any way.
words = sentence.split(" ")

# PART 1: Print out the `words` variable to see 
# the list of words that was created from 
# splitting the sentence.

print(words)

# PART 2: Create a function called `count`. It 
# should take a string and return the number of 
# times that word appears in the sentence. 
# (Make use of the `words` list!)
### count("and") should return 4
### count("is") should return 1
### count("programmer") should return 2

def count(w):
  word_count = 0
  for i in range(len(words)): 
    if w == words[i]:
      word_count = word_count + 1    
  return word_count 

print(count("and")) # 4
print(count("is")) # 1
print(count("programmer")) # 2

# PART 3: Find the word that appears the MOST in 
# the sentence, and print out that word. Use the 
# `count()` function to make this process easier.
### Expected: `a`, because it appears 5 times.

most_common_word = ""
frequency = 0

for item in words:
  current_word = item
  current_frequency = count(item)
  if current_frequency > frequency:
    frequency = current_frequency
    most_common_word = current_word

print(most_common_word)