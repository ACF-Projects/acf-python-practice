from passcrack import single_guess, multi_guess
import string
import time

passguess = input("Type a word you'd like the computer to guess (3-4 characters recommended). ")
look_for = ""

confirm = input("""Check for what? Type one word with all desired characters (ex: 'luns' for all). 
\tLowercase: 'l'\tUppercase: 'u'\tNumbers: 'n'\tSymbols: 's'.\n""")
if "l" in confirm:
    look_for += string.ascii_lowercase
if "u" in confirm:
    look_for += string.ascii_uppercase
if "n" in confirm:
    look_for += string.digits
if "s" in confirm:
    look_for += string.punctuation

debug = ""
while debug != "yes" and debug != "no":
    debug = input("Do you want to debug? Type YES or NO ").lower()

################################################################
# Single thread execution
################################################################
start_time = time.time()
single_attempts = single_guess(passguess, look_for, debug == "yes")
single_guess_time = time.time() - start_time

################################################################
# Multiple thread execution
################################################################
start_time = time.time()
multi_attempts = multi_guess(passguess, look_for, debug == "yes")
multi_guess_time = time.time() - start_time

print(f"Single guess took {single_guess_time} seconds. Looked at {single_attempts} different combinations.")
print(f"Multi guess took {multi_guess_time} seconds. Looked at {multi_attempts} different combinations.")
