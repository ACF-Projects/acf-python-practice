import mystack

"""
Here, your task is to implement the Stack data
structure using Python's list structure. Find
out which methods you need to implement in
`mystack.py`!

Then, afterwards, your job is to implement the
`is_valid_parentheses` function below. Read the
function comment below to learn more about it.

We've provided some code already that runs the
function against multiple "test cases". These are
cases that will make sure your code is running as
intended; you should see everything "pass the test
case" if your code is written correctly. :)

If there are any questions about this
assignment, feel free to ask questions!
"""

def is_valid_parentheses(str):
  """
  When given a string `str` that holds a
  combination of open and closed parentheses,
  should return True if the parentheses are
  correctly opened and closed. Or else,
  should return False.
  """
  stack = mystack.Stack()
  pairs = {")": "(", "]": "[", "}": "{"}
  # Your code here
  
cases = open("test.txt")
for s in cases.readlines():
  s = s.strip().split(" ")
  res = is_valid_parentheses(s[0])
  exp = s[1] == "True"
  if res == exp:
    print(s[0] + " passed the test case!")
  else:
    print(s[0] + " failed the test case.")