# PASSWORD STRENGTH

# Below is a list of strings called "passwords".
# Every string represents somebody's password.
# You do NOT need to modify this list.
passwords = ["hi", 
             "ACF15COOL#000?",
             "123",
             "rubber__ducky",
             "P4SSW0RD",
             "pie-thon1",
             "bye",
             "apple"]

# PART 1: For every password in the list, print 
# a message in the following format:
# (password) is (weak/normal/strong)
# If a password is 0-6 chars long, it is WEAK.
# If a password is 7-10 chars long, it is NORMAL.
# If a password is 11+ chars long, it is STRONG.

for password in passwords:
  if len(password) >= 0 and len(password) <= 6:
    print("It is WEAK")
  elif len(password) >= 7 and len(password) <= 10:
    print("It is NORMAL")
  else:
    print("It is STRONG")

# PART 2: For every password in the list, while 
# a password is WEAK (0-6 characters long), add 
# "0"s to the end of it until it has 7 characters.
# Ex: "hi" should become "hi00000"
# Ex: "pie-thon1" should remain "pie-thon1"
# Then, print out the list.

for i in range(len(passwords)):
  while len(passwords[i]) <= 6:
    passwords[i] = passwords[i] + "0"

print(passwords)