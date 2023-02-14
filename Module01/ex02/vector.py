class Vector:
    """ Vector class for linear algebra  """

    def __init__(self, arg):
        if isinstance(arg, list):
            self.values = []
            if len(arg) == 1:
                self.values.insert(0, arg[0].copy())
                self.shape = (1, len(arg[0]))
            else:
                for i in range(len(arg)):
                    self.values.insert(i, arg[i].copy())
                self.shape = (len(arg), 1)
        elif isinstance(arg, (int, float)):
            self.values = [[42] * 1 for i in range(arg)]
            for i in range(arg):
                self.values[i][0] = float(i)
            self.shape = (arg, 1)
        elif isinstance(arg, tuple):
            interval = arg[1] - arg[0]
            if interval < 0:
                raise ValueError("arg[1] must be greater than arg[0]")
            self.values = [[42] * 1 for i in range(interval)]
            for i in range(interval):
                self.values[i][0] = float(i + arg[0])
            self.shape = (interval, 1)
        else:
            raise TypeError("arg must be a list, int or a tuple")

    def dot(self, v):
        """ returns the dot product of two vectors """
        if not isinstance(v, Vector):
            raise TypeError("must be a Vector")
        if self.shape[0] != v.shape[0] or self.shape[1] != v.shape[1]:
            raise ValueError("vectors must have the same shape")
        ret = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret += self.values[i][j] * v.values[i][j]
        return ret

    def T(self):
        """ returns the transpose of the vector """
        t_value = [[42] * self.shape[0] for i in range(self.shape[1])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                t_value[j][i] = self.values[i][j]
        return Vector(t_value)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("must be a number")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] *= n
        return ret

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("must be a number")
        if n == 0:
            raise ZeroDivisionError("division by zero.")

        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] /= n
        return ret

    def __rtruediv__(self, v):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __add__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("must be a Vector")
        if self.shape[0] != v.shape[0] or self.shape[1] != v.shape[1]:
            raise ValueError("vectors must have the same shape")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] += v.values[i][j]
        return ret

    def __radd__(self, v):
        raise NotImplementedError("Addition of a scalar to a Vector is not defined here.")

    def __sub__(self, v):
        if not isinstance(v, Vector):
            raise TypeError("must be a Vector")
        if self.shape[0] != v.shape[0] or self.shape[1] != v.shape[1]:
            raise ValueError("vectors must have the same shape")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] -= v.values[i][j]
        return ret

    def __rsub__(self, v):
        raise NotImplementedError("Subtraction of a scalar from a Vector is not defined here.")

    def __str__(self):
        ret = "Vector("
        ret += str(self.values)
        ret += ")"
        return ret

    def __repr__(self):
        return self.__str__() + " | Shape: " + str(self.shape)


