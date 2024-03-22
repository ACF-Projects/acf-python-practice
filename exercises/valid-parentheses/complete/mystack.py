class Stack:
  
  def __init__(self):
    """
    When a stack is created, it should create
    and persistently store an empty array.
    """
    self.a = []
    
  def push(self, elem):
    """
    The push function takes in an element `elem`
    and adds it to the end of the array.

    This function does not return anything.
    """
    self.a.append(elem)
    
  def pop(self):
    """
    The pop function takes no arguments and
    returns the element at the end of the array.

    If the array is empty, this returns `None`.
    """
    if self.is_empty():
      return None
    return self.a.pop()
    
  def is_empty(self):
    """
    The is_empty function returns `True` if the
    array is empty, and `False` if otherwise.
    """
    return self.a == []