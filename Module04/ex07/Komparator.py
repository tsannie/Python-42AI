import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("data must be a pandas DataFrame")
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            raise ValueError("categorical_var and numerical_var must be strings")
        df = self.data[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()
        fig, ax = plt.subplots(nrows=len(features))
        for i, feature in enumerate(features):
            df[df[categorical_var] == feature][numerical_var].plot.box(ax=ax[i], title=feature)
        plt.tight_layout()
        plt.show()

    def density(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            raise ValueError("categorical_var and numerical_var must be strings")
        df = self.data[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()
        fig, ax = plt.subplots(nrows=len(features))
        for i, feature in enumerate(features):
            ax[i].set_title(feature)
            sns.kdeplot(df[df[categorical_var] == feature][numerical_var], ax=ax[i], fill=True, label=feature)
        plt.tight_layout()
        plt.show()



    def compare_histograms(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            raise ValueError("categorical_var and numerical_var must be strings")
        df = self.data[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()
        fig, ax = plt.subplots(nrows=len(features))
        for i, feature in enumerate(features):
            df[df[categorical_var] == feature][numerical_var].plot.hist(ax=ax[i], title=feature)
        plt.tight_layout()
        plt.show()

