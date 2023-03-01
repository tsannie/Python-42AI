import sys
import numpy as np
import matplotlib.pyplot as plt
from csvreader import CsvReader as csv

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        if not isinstance(max_iter, int):
            print("Error: max_iter is not an integer.")
            exit()
        if not isinstance(ncentroid, int):
            print("Error: ncentroid is not an integer.")
            exit()
        if max_iter < 1:
            print("Error: max_iter is less than 1.")
            exit()
        if ncentroid < 1:
            print("Error: ncentroid is less than 1.")
            exit()
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids



    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        -----
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        -------
        Return:
        None.
        -------
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(X, np.ndarray):
            print("Error: X is not a numpy.ndarray.")
            exit()
        if self.ncentroid > X.shape[0]:
            print("Error: ncentroid is greater than the number of data points.")
            exit()
        for i in range(self.ncentroid):
            self.centroids.append(X[i])

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        -----
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        -------
        Return:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        -------
        Raises:
        This function should not raise any Exception.
        """


if __name__ == "__main__":

    args = {key: value for arg in sys.argv[1:] for key, value in [arg.split("=")]}
    if len(args) != 3 or "filepath" not in args or "ncentroid" not in args or "max_iter" not in args:
        print("Usage: python Kmeans.py  filepath=[path_to_dataset] ncentroid=[ncentroid] max_iter=[max_iter]")
        exit()
    print(args)


    with csv(args["filepath"], header=True) as file:
        data = file.getdata()
        data = np.array(data).astype(float)

    print(data)

    plt.scatter(data[:, 1], data[:, 2])
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.show()

    kc = KmeansClustering(int(args["max_iter"]), int(args["ncentroid"]))
    #kc.fit(data)




