from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")
# Output :
# Loading image of dimensions 200 x 200

cf = ColorFilter()

invert = cf.invert(arr)
imp.display(invert)

green = cf.to_green(arr)
imp.display(green)

blue = cf.to_blue(arr)
imp.display(blue)

red = cf.to_red(arr)
imp.display(red)

celluloid = cf.to_celluloid(arr)
imp.display(celluloid)

grayscale = cf.to_grayscale(arr, "m")
imp.display(grayscale)

grayscale = cf.to_grayscale(arr, "weight", weights=[0.2, 0.3, 0.5])
imp.display(grayscale)
