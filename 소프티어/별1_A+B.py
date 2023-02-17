import sys

def solution1():
    t = int(sys.stdin.readline())
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print("Case #{}:".format(i+1), a + b)


if __name__ == "__main__":
    solution1()
