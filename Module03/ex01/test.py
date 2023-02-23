from ImageProcessor import ImageProcessor

imp = ImageProcessor()

arr = imp.load("non_existing_file.png")
# Output :
#Exception: FileNotFoundError -- strerror: No such file or directory
print(arr)
# Output :
#None
print()

arr = imp.load("empty_file.png")
# Output :
#Exception: OSError -- strerror: None
print(arr)
# Output :
#None
print()

arr = imp.load("../resources/42AI.png")
# Output :
#Loading image of dimensions 200 x 200
print(arr)
print(arr.dtype)
print()

imp.display(arr)
