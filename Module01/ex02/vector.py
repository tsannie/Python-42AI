import numpy as np

class Vector:
    """ Vector class for linear algebra  """

    def __init__(self, list_of_values):
        if len(list_of_values) == 1:
            print("len(args[0] = ", len(list_of_values))
            self.values = np.array(list_of_values[0])
            self.shape = (len(list_of_values[0]), 1)
        else:
            self.values = np.array(list_of_values)
            self.shape = (1, len(list_of_values))
        print(self.shape)
        print(self.values)

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
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                ret += "{:.1f}".format(self.values[i])
                if i != len(self.values) - 1:
                    ret += ", "
        else:
            for i in range(self.shape[0]):
                ret += "{:.1f}".format(i)
                if i != len(self.values) - 1:
                    ret += ", "

            """ for i in range(len(self.values)):
                ret += "{:.1f}".format(self.values[i][0])
                if i != len(self.values) - 1:
                    ret += ", " """
        ret += "])"
        return ret

