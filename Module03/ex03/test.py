from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
# Output :
#Loading image of dimensions 200 x 200



cf = ColorFilter()
""" invert = cf.invert(arr)
imp.display(invert)

cf.to_green(arr)
green = cf.to_green(arr)
imp.display(green)

cf.to_blue(arr)
blue = cf.to_blue(arr)
imp.display(blue)

cf.to_red(arr)
red = cf.to_red(arr)
imp.display(red)

cf.to_celluloid(arr)
celluloid = cf.to_celluloid(arr)
imp.display(celluloid) """

cf.to_grayscale(arr, 'm')
grayscale = cf.to_grayscale(arr, 'm')
imp.display(grayscale)


"""
cf.to_grayscale(arr, ’m’)
cf.to_grayscale(arr, ’weight’, weights = [0.2, 0.3, 0.5]) """
