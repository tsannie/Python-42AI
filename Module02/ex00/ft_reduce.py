def ft_reduce(function_to_apply, iterable):
  """Apply function of two arguments cumulatively.
  Args:
  function_to_apply: a function taking an iterable.
  iterable: an iterable object (list, tuple, iterator).
  Return:
  A value, of same type of elements in the iterable parameter.
  None if the iterable can not be used by the function.
  """

  if not hasattr(iterable, '__iter__'):
    raise TypeError("ft_reduce() object is not iterable")

  for i in iterable:
    if i == iterable[0]:
      result = i
    else:
      result = function_to_apply(result, i)
  return result

