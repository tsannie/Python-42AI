import pandas as pd

class FileLoader:

    def load(self, path):
        try:
            data = pd.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(data.shape[0], data.shape[1]))
            return data
        except:
            print("Error: File not found")
            return None

    def display(self, df, n):
        if not isinstance(df, pd.DataFrame):
            print("Error: Data is not a pandas DataFrame")
            return None
        if n >= 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
        else:
            print("Error: n is null")

