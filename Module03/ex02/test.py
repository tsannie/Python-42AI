import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()

arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
#Output :
#array([[5],
#[10],
#[15]])
print()

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2, 3, 0))
#Output :
#array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
#[’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)
print()

