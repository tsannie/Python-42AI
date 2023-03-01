from PIL import Image
import numpy as np

class ImageProcessor:
    """ImageProcessor class"""

    @staticmethod
    def load(path):
        """Loads an image from a file as a numpy array"""
        try:
          img = Image.open(path)
          img.load()
          arr = np.array(img)
          print("Loading image of dimensions {} x {}".format(img.size[0], img.size[1]))
          img_array = np.divide(arr[:,:,0:3], 255)
          return img_array.astype(np.float32)
        except FileNotFoundError:
          print("Exception: FileNotFoundError -- strerror: No such file or directory")
        except OSError:
          print("Exception: OSError -- strerror: None")
        return None

    @staticmethod
    def display(array):
        """Displays an image from a numpy array"""
        if array is None:
            print("Exception: TypeError -- strerror: None")
            return
        if not isinstance(array, np.ndarray):
            print("Exception: TypeError -- strerror: None")
            return
        img = Image.fromarray(np.multiply(array, 255).astype(np.uint8))
        img.show()

