class Evaluator:
    def zip_evaluate(coefs, words):
      """Evaluates a list of words based on a given list of coefficients using zip."""
      if len(coefs) != len(words):
        return -1
      n = 0
      for i in zip(coefs, words):
        n += i[0] * len(i[1])
      return n

    def enumerate_evaluate(coefs, words):
      """Evaluates a list of words based on a given list of coefficients using enumerate."""
      if len(coefs) != len(words):
        return -1
      n = 0
      for i in enumerate(words):
        n += coefs[i[0]] * len(i[1])
      return n
