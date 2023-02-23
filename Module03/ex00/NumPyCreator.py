import numpy as np

class NumPyCreator:
    """This class will help you manipulate lists and tuples into numpy arrays"""

    def from_list(self, lst):
        """"takes a list or nested lists and returns its corresponding Numpy array"""

        return np.array(lst, dtype=object)

    def from_tuple(self, tpl):
        """"takes a tuple or nested tuples and returns its corresponding Numpy array"""
        return np.array(tpl)

    def from_iterable(self, itr):
        """"takes an iterable and returns an array which contains all its elements."""
        return np.array(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.random(shape)

    def identity(self, n):
        return np.identity(n)
