import sys

def solution1():
    a, b = map(int, sys.stdin.readline().split())
    if a > b: print('A')
    elif a < b: print('B')
    else: print('same')


if __name__ == "__main__":
    solution1()
