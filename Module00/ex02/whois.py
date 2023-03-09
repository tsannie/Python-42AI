import sys

def check_number(num):
  if num == 0:
    print("The number is zero.")
  elif num % 2 == 0:
    print("The number is even.")
  else:
    print("The number is odd.")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python whois.py <number>")
    sys.exit(1)

  try:
    num = int(sys.argv[1])
  except ValueError:
    print("Error: Please provide exactly one integer argument.")
    sys.exit(1)
  check_number(num)
