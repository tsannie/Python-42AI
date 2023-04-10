import numpy as np


class ColorFilter:
    """Apply a variety of color filters on images"""

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None
        return 1 - array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None

        new = np.zeros(array.shape, dtype=np.float32)
        new[:, :, 2] = array[:, :, 2]

        return new

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None

        new = np.zeros(array.shape, dtype=np.float32)
        new[:, :, 1] = array[:, :, 1]

        return new

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None

        new = np.zeros(array.shape, dtype=np.float32)
        new[:, :, 0] = array[:, :, 0]

        return new

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None

        new = np.zeros(array.shape, dtype=np.float32)
        min = array.min()
        max = array.max()
        shades = np.linspace(min, max, 4, endpoint=False)
        for shade in shades:
            new[array >= shade] = shade
        return new

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None:
            return None
        if not isinstance(array, np.ndarray):
            return None
        if filter not in ["m", "mean", "w", "weight"]:
            return None

        if filter in ["m", "mean"]:
            new = array.copy()
            for colomn in new:
                for pixel in colomn:
                    color = np.sum(pixel) / 3
                    pixel[0] = color
                    pixel[1] = color
                    pixel[2] = color
            return new
        elif filter in ["w", "weight"]:
            # check weights
            if "weights" not in kwargs:
                return None
            weights = kwargs["weights"]
            if len(weights) != 3:
                return None
            if np.sum(weights) != 1:
                return None
            new = array.copy()
            for colomn in new:
                for pixel in colomn:
                    color = np.sum(pixel * weights)
                    pixel[0] = color
                    pixel[1] = color
                    pixel[2] = color
            return new
