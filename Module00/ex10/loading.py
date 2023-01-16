import sys
import time

def ft_progress(listy):
    print("ETA: 0:00:00", end="\r")

listy = range(100000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
time.sleep(0.01)
print()
print(ret)
