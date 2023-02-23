import numpy as np

def check_type(obj, dtype):
    if not isinstance(obj, dtype) or not isinstance(obj[0], (list, tuple)):
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
    def from_iterable(itr):
        return np.array(itr)

    @staticmethod
    def from_shape(shape, value=0):
        return np.full(shape, value)

    @staticmethod
    def random(shape):
        return np.random.random(shape)

    @staticmethod
    def identity(n):
        return np.identity(n)

a = NumPyCreator().from_list([[1,2,3],['a','b','c'],[6,4,7]])
