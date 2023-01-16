import sys
import string

def error():
    print("ERROR")
    exit()

def filterwords(n, s):
    filtered = []
    words = s.split()
    for word in words:
        no_punct = word.translate(str.maketrans('', '', string.punctuation))
        if len(no_punct) > n:
            filtered.append(no_punct)
    print(filtered)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        error()

    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except:
        error()

    if not isinstance(s, str) or not isinstance(n, int):
        error()

    filterwords(n, s)


