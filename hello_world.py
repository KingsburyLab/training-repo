"""
A simple python file containing a function definition
"""

def add_numbers(nums: list):
  """
  Add numbers provided in a list
  
  Args:
    nums: a list of numbers to add
    
  Returns:
    The sum of numbers in the list
    
  Example::
  
    >>> add_numbers([1,2,3,4])
    10
  """
  return sum(nums)
