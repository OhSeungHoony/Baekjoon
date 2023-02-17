import sys

def solution1():
    ans = 0
    for _ in range(5):
        start, end = map(str, sys.stdin.readline().split())
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        if sm <= em:
            m = em - sm
            h = eh - sh
        else:
            m = 60 + em - sm
            h = eh - sh - 1
        ans += m + 60 * h
    print(ans)


if __name__ == "__main__":
    solution1()
