import pandas as pd
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("data must be a pandas DataFrame")
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        self.data.boxplot(column=numerical_var, by=categorical_var)
        plt.show()
