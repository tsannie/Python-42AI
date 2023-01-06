def text_analyzer(str=None):
  if str is None:
    str = input(">> ")

  upper = 0
  lower = 0
  punct = 0
  space = 0

  for c in str:
    if c.isupper():
      upper += 1
    elif c.islower():
      lower += 1
    elif c.isspace():
      space += 1
    else:
      punct += 1

  print("The text contains", len(str), "character(s):")
  print("-", upper, "upper letter(s)")
  print("-", lower, "lower letter(s)")
  print("-", punct, "punctuation mark(s)")
  print("-", space, "space(s)")
