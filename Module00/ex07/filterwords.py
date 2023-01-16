import sys

def error():
    print("ERROR")
    exit()

def filterwords(n, s):
    words = s.split()
    for word in words:
        if word
        if len(word) > n:
            print(word)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        error()

    n = sys.argv[1]
    s = sys.argv[2]
    if not isinstance(s, str) or not isinstance(n, int):
        error()

    filterwords(n, s)


