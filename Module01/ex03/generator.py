import random

def shuffle(text):
  """Shuffles the text."""
  for i in range(len(text)):
    j = random.randint(0, len(text) - 1)
    text[i], text[j] = text[j], text[i]



def generator(text, sep=" ", option=None):
  """Splits the text according to sep value and yield the substrings.
  option precise if a action is performed to the substrings before it is yielded.
  """
  if not isinstance(text, str) or option not in ["shuffle", "unique", "ordered", None]:
    yield "ERROR"
  else:
    text = text.split(sep)
    if option == "shuffle":
      shuffle(text)
      for word in text:
        yield word
    elif option == "unique":
      text = set(text)
      for word in text:
        yield word
    elif option == "ordered":
      text = sorted(text)
      for word in text:
        yield word
    elif option == None:
      for word in text:
        yield word

