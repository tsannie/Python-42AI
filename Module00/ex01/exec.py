import sys

def reverse_and_swap(string):
  # Reverse the string
  reversed_str = string[::-1]

  # Swap the case of the characters
  swapped_string = ""
  for char in reversed_str:
    if char.islower():
      swapped_string += char.upper()
    else:
      swapped_string += char.lower()

  # Print the modified string
  print(swapped_string)

# Get the command line arguments
args = sys.argv[1:]

# If no argument is provided, print an usage message
if not args:
  print("Usage: python exec.py [string]")
else:
  # Merge the arguments into a single string
  string = " ".join(args)

  # Call the reverse_and_swap function
  reverse_and_swap(string)
