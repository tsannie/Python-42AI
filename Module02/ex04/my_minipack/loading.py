import sys
import time

def ft_progress(listy):
    size = len(listy)
    start = time.time()
    for i in listy:
        time_spent = time.time() - start
        percent = (i + 1) / size
        eta = time_spent / percent - time_spent
        bar = int(percent * 40)

        print("ETA: {:5.2f}s [{:3d}%] [{}{}] {:4}/{} | elapsed time {:5.2f}s".format(
            eta,
            int(percent * 100),
            ("=" * bar) + (">" if bar < 40 else "="), " " * (40 - bar),
            i + 1, size, time_spent), end="\r")
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
