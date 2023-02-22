from math import sqrt
import numpy as np

class TinyStatistician:

    def mean(self, x):
        if type(x) is not list and type(x) is not np.ndarray or len(x) == 0:
            return None
        sum = 0
        for i in x:
            sum += i
        return sum / len(x)

    def median(self, x):
        if type(x) is not list and type(x) is not np.ndarray or len(x) == 0:
            return None
        x_sorted = x.copy()
        x_sorted.sort()
        i = int(len(x) / 2)
        if not len(x_sorted) % 2:
            return (x_sorted[i] + x_sorted[i - 1]) / 2
        return x_sorted[i]

    def quartile(self, x):
        if type(x) is not list and type(x) is not np.ndarray or len(x) == 0:
            return None
        x_sorted = x.copy()
        x_sorted.sort()
        i = int(len(x) / 4)
        if not len(x_sorted) % 4:
            q1 = (x_sorted[i] + x_sorted[i - 1]) / 2
            q3 = (x_sorted[i * 3] + x_sorted[i * 3 - 1]) / 2
            return [q1, q3]
        return [x_sorted[i], x_sorted[i * 3]]

    def var(self, x):
        if type(x) is not list and type(x) is not np.ndarray or len(x) == 0:
            return None
        mean = self.mean(x)
        ss = 0
        for i in x:
            ss += (i - mean) ** 2
        return ss / (len(x))

    def std(self, x):
        if type(x) is not list and type(x) is not np.ndarray or len(x) == 0:
            return None
        return sqrt(self.var(x))
