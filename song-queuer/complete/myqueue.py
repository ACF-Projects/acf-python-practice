class Queue:
  
  def __init__(self):
    """
    When a queue is created, it should create
    and persistently store an empty array.
    """
    self.a = []
    
  def enqueue(self, elem):
    """
    The enqueue function takes in an element `elem`
    and adds it to the end of the array.

    This function does not return anything.
    """
    self.a.append(elem)
    
  def dequeue(self):
    """
    The dequeue function takes no arguments and
    returns the element at the START of the array.

    If the array is empty, this returns `None`.
    """
    if self.is_empty():
      return None
    return self.a.pop(0)
    
  def is_empty(self):
    """
    The is_empty function returns `True` if the
    array is empty, and `False` if otherwise.
    """
    return self.a == []