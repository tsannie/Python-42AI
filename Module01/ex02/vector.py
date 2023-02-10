class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def __str__(self):
        return str(self.values)

