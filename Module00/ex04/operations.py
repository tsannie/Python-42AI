import sys

def main(A, B):
  print("Sum:        ", A + B)
  print("Difference: ", A - B)
  print("Product:    ", A * B)
  try:
    print("Quotient:   ", A / B)
  except ZeroDivisionError:
    print("Quotient:    ERROR (div by zero)")
  try:
    print("Remainder:  ", A % B)
  except ZeroDivisionError:
    print("Remainder:   ERROR (modulo by zero)")

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>")
  elif len(sys.argv) != 3:
    print("AssertionError: too many arguments")
  else:
    try:
      A = int(sys.argv[1])
      B = int(sys.argv[2])
      main(A, B)
    except ValueError:
      print("AssertionError: only integers")
