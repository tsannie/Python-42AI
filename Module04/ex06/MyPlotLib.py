import matplotlib.pyplot as plt
import pandas as pd


class MyPlotLib:
    def _entry_check(self, data, features):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("data must be a pandas DataFrame")
        if not isinstance(features, list):
            raise ValueError("features must be a list")
        for feature in features:
            if feature not in data.columns:
                raise ValueError("feature not in data")

    def histogram(self, data, features):
        self._entry_check(data, features)
        data[features].hist()
        plt.show()

    def density(self, data, features):
        self._entry_check(data, features)
        data[features].plot.density()
        plt.show()

    def pair_plot(self, data, features):
        self._entry_check(data, features)
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    def box_plot(self, data, features):
        self._entry_check(data, features)
        data.boxplot(features)
        plt.show()
