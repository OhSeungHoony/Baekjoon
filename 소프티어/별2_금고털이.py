import sys

def solution1(): # 틀림
    w, n = map(int, sys.stdin.readline().split())
    # things = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    things = {}
    for _ in range(n):
        kin, val = map(int, sys.stdin.readline().split())
        things[val] = kin
    sorted_things = sorted(things.items())

    ans = 0
    while True:
        if w <= sorted_things[-1][1]:
            ans += w * sorted_things[-1][0]
            break
        else:
            ans += sorted_things[-1][0] * sorted_things[-1][1]
            w -= sorted_things[-1][1]
            sorted_things.pop()
    print(ans)

def solution2():
    w, n = map(int, sys.stdin.readline().split())
    things = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    things.sort(key=lambda x: x[1], reverse=True)

    ans = 0
    for weight, val in things:
        if w > weight:
            ans += weight * val
            w -= weight
        else:
            ans += w * val
            break
    print(ans)


if __name__ == "__main__":
    # solution1()
    solution2()
