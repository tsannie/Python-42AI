import pandas as pd


class SpatioTemporalData:
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            print("Error: data is not a pandas DataFrame")
        self.data = data

    def when(self, location):
        return list(self.data[self.data["City"] == location]["Year"].unique())

    def where(self, year):
        return list(self.data[self.data["Year"] == year]["City"].unique())
