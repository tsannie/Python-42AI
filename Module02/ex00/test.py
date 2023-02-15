from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# Example 1:
print("Example 1:")
x = [1, 2, 3, 4, 5]
t = ft_map(lambda dum: dum + 1, x)
print(t)
# Output:
#<generator object ft_map at 0x7f708faab7b0> # The adress will be different
t = list(ft_map(lambda t: t + 1, x))
print(t)
# Output:
#[2, 3, 4, 5, 6]
try:
    t = list(ft_map(lambda t: t + 1, 10))
except TypeError as e:
    print(e)
# Output:
#ft_map() object is not iterable
print()

print("Example 2:")
# Example 2:
t = ft_filter(lambda dum: not (dum % 2), x)
print(t)
# Output:
#<generator object ft_filter at 0x7f709c777d00> # The adress will be different
t = list(ft_filter(lambda dum: not (dum % 2), x))
print(t)
# Output:
#[2, 4]
try:
    t = list(ft_filter(lambda dum: not (dum % 2), 10))
except TypeError as e:
    print(e)
# Output:
#ft_filter() object is not iterable
print()

print("Example 3:")
# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
t = ft_reduce(lambda u, v: u + v, lst)
print(t)
# Output:
"Hello world"
try:
    t = ft_reduce(lambda u, v: u + v, 10)
except TypeError as e:
    print(e)
# Output:
#ft_reduce() object is not iterable
