import numpy as np
from TinyStatistician import TinyStatistician

print("Test mean:")
t = TinyStatistician()
a = [1, 42, 300, 10, 59]
nplist = np.array(a)

print(t.mean(nplist))
#output: 82.4
print(t.mean(a))
#output: 82.4
print(t.mean([]))
#output: None
print(t.mean(42))
#output: None
print(round(t.mean(a + [42.42]), 2))
#output: 75.74
print()

print("Test median:")
print(t.median(a))
#output: 42
print(t.median([1, 4, 3, 2]))
#output: 2.5
print(t.median([]))
#output: None
print()

print("Test quartiles:")
print(t.quartile(a))
#output: [10, 59]
print(t.quartile([8, 4, 5, 2, 6, 1, 3, 7]))
#output: [2.5, 6.5]
print(t.quartile([]))
#output: None
print()

print("Test variance:")
print(t.var(a))
#output: 12279.439999999999
print(t.var([1, 2, 3, 4, 5]))
#output: 2.0
print(t.var([]))
#output: None
print()

print("Test standard deviation:")
print(t.std(a))
#output: 110.81263465868862
print(t.std([1, 2, 3, 4, 5]))
#output: 1.4142135623730951
print(t.std([]))
#output: Non
