import sys

def reverse_and_swap(string):
  reversed_str = string[::-1]

  swapped_string = ""
  for char in reversed_str:
    if char.islower():
      swapped_string += char.upper()
    else:
      swapped_string += char.lower()

  print(swapped_string)

args = sys.argv[1:]

if not args:
  print("Usage: python exec.py [string]")
else:
  string = " ".join(args)
  reverse_and_swap(string)
