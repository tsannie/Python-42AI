from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print("Testing from_list:")
a = npc.from_list([[1, 2, 3], [6, 3, 4]])
print(a)
# Output :
# array([[1, 2, 3],
# [6, 3, 4]])
a = npc.from_list([[1, 2, 3], [6, 4]])
print(a)
# Output :
# None
a = npc.from_list([[1, 2, 3], ["a", "b", "c"], [6, 4, 7]])
print(a)
print("dtype= ", a.dtype)
# Output :
# array([['1','2','3'],
# ['a','b','c'],
# ['6','4','7'], dtype='<U21'])
npc.from_list(((1, 2), (3, 4)))
# Output :
# None
print()

print("Testing from_tuple:")
a = npc.from_tuple(("a", "b", "c"))
print(a)
# Output :
# array(['a', 'b', 'c'])
a = npc.from_tuple(["a", "b", "c"])
print(a)
# Output :
# None
print()

print("Testing from_iterable:")
a = npc.from_iterable(range(5))
print(a)
# Output :
# array([0, 1, 2, 3, 4])
print()

print("Testing from_shape:")
shape = (3, 5)
a = npc.from_shape(shape)
print(a)
# Output :
# array([[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]])
print()

print("Testing random:")
a = npc.random(shape)
print(a)
# Output :
# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
print()

print("Testing identity:")
a = npc.identity(4)
print(a)
# Output :
# array([[1., 0., 0., 0.],
# [0., 1., 0., 0.],
# [0., 0., 1., 0.],
# [0., 0., 0., 1.]])
