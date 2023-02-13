import numpy as np

class Vector:
    """ Vector class for linear algebra  """

    def __init__(self, *args):
        self.values = np.array(args)
        print(len(args))
        self.shape = len(args) == 1 and (1, len(args)) or (len(args), 1)
        print(self.shape)

    def dot(self, v):
        return np.dot(self.values, v.values)

    def T(self):
        return np.transpose(self.values)

    def __add__(self, n):
        ret = np.add(self.values, n)
        if self.shape[0] == 1:
            return Vector(ret[0])
        return Vector(ret)

    def __sub__(self, n):
        return np.subtract(self.values, n)

    def __mul__(self, n):
        return np.multiply(self.values, n)

    def __rmul__(self, n):
        return np.multiply(self.values, n)

    def __truediv__(self, n):
        return np.divide(self.values, n)

    def __str__(self):
        ret = "Vector(["
        for i in range(len(self.values)):
            ret += "{:.1f}".format(self.values[i][0])
            if i != len(self.values) - 1:
                ret += ", "
        ret += "])"
        return ret

