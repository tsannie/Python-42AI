import string
import sys

def text_analyzer(arg=None):
  """
  This function counts the number of upper characters, lower characters,
  punctuation and spaces in a given text.
  """
  if arg is None:
    arg = input(">> ")
  if not isinstance(arg, str):
    print("AssertionError: argument is not a string")
    return

  upper = 0
  lower = 0
  punct = 0
  space = 0

  for c in arg:
    if c.isupper():
      upper += 1
    elif c.islower():
      lower += 1
    elif c.isspace():
      space += 1
    elif c in (string.punctuation):
      punct += 1

  print("The text contains", len(arg), "character(s):")
  print("-", upper, "upper letter(s)")
  print("-", lower, "lower letter(s)")
  print("-", punct, "punctuation mark(s)")
  print("-", space, "space(s)")


if __name__ == "__main__":
  if (len(sys.argv) > 1):
    print("Usage: python count.py <text>")
  else:
    text_analyzer()
