import numpy as np

def check_type(obj, dtype):
    if not isinstance(obj, dtype):
        return False
    for i in range(len(obj)):
        if not isinstance(obj[i], type(obj[0])) or len(obj[i]) != len(obj[0]):
            return False
    return True



class NumPyCreator:

    @staticmethod
    def from_list(lst, dtype=None):
        if check_type(lst, list):
            return np.array(lst, dtype)
        return None

    @staticmethod
    def from_tuple(tpl, dtype=None):
        if check_type(tpl, tuple):
            return np.array(tpl, dtype)
        return None

    @staticmethod
    def from_iterable(itr, dtype=None):
        return np.array(itr, dtype)

    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    @staticmethod
    def random(shape, dtype=None):
        return np.full(shape, np.random.random_sample(shape), dtype)

    @staticmethod
    def identity(n):
        return np.identity(n)
