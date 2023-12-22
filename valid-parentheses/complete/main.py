import mystack
import os

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
  for bracket in str:
    if bracket == "{" or bracket == "[" or bracket == "(":
      stack.push(bracket)
    elif bracket == "}" or bracket == "]" or bracket == ")":
      if stack.is_empty():
        return False
      if pairs[bracket] != stack.pop():
        return False
  return stack.is_empty()

cases = open(os.path.dirname(__file__) + "/../test.txt")
for s in cases.readlines():
  s = s.strip().split(" ")
  res = is_valid_parentheses(s[0])
  exp = s[1] == "True"
  if res == exp:
    print(s[0] + " passed the test case!")
  else:
    print(s[0] + " failed the test case.")