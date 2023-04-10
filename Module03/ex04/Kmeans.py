import sys
import numpy as np
import matplotlib.pyplot as plt
from csvreader import CsvReader as csv
from mpl_toolkits.mplot3d import Axes3D


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
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
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids
        self.last_scores = 0.0  # last score of the centroids
        self.stable = False  # True if the centroids are stable

        # plt
        self.ax = plt.axes(projection="3d")

    def distance(self, x, y):
        return np.square(np.sum((x - y) ** 2))

    def display(self, data, c, i):
        # output
        print("##########################")
        print("Iteration {}:".format(i + 1))
        for e in range(self.centroids.shape[0]):
            print("Centroid {}: {}".format(e + 1, self.centroids[e]))
            print("Number of data points in cluster: {}".format(np.sum(c == e)))
            print()
        print("Score: {:.2f}".format(self.last_scores))

        # plt
        self.ax.clear()
        self.ax.set_xlabel("height")
        self.ax.set_ylabel("weight")
        self.ax.set_zlabel("bone_density")
        self.ax.set_title("solar_system_census")
        self.ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=c)
        self.ax.scatter(
            self.centroids[:, 0],
            self.centroids[:, 1],
            self.centroids[:, 2],
            c="red",
            marker="x",
        )
        plt.pause(1)

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

        t = np.random.choice(X.shape[0], self.ncentroid, replace=False)
        self.centroids = X[t]

        for i in range(self.max_iter):
            i_min = self.predict(X)
            for j in range(self.centroids.shape[0]):
                self.centroids[j] = np.mean(X[i_min == j], axis=0)
            self.display(X, i_min, i)
            if self.stable:
                break

        plt.show()

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
        dist = np.zeros((X.shape[0], self.ncentroid))
        for i in range(self.centroids.shape[0]):
            for e in range(X.shape[0]):
                dist[e][i] = self.distance(X[e], self.centroids[i])
        i_min = np.argmin(dist, axis=1)

        score = 0.0
        for i in range(dist.shape[0]):
            score += dist[i][i_min[i]]
        if score == self.last_scores:
            self.stable = True
        self.last_scores = score

        return i_min


def fatal():
    print(
        "Usage: python Kmeans.py  filepath=[path_to_dataset] ncentroid=[ncentroid] max_iter=[max_iter]"
    )
    exit()


if __name__ == "__main__":
    a = {}
    for arg in sys.argv[1:]:
        s = arg.split("=")
        if (
            len(s) != 2
            or s[0] not in ["filepath", "ncentroid", "max_iter"]
            or s[0] in a
        ):
            fatal()
        a[s[0]] = s[1]

    print(a)

    if "ncentroid" not in a:
        a["ncentroid"] = 4
    if "max_iter" not in a:
        a["max_iter"] = 20

    with csv(a["filepath"], header=True) as file:
        data = file.getdata()
        data = np.array(data).astype(float)
    data = data[:, 1:]

    try:
        kc = KmeansClustering(int(a["max_iter"]), int(a["ncentroid"]))
        kc.fit(data)
    except:
        fatal()
