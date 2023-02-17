import sys

def solution1():
    n, m = map(int, sys.stdin.readline().split())
    nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    mList = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    diffList = []

    while True:
        if nList == [] or mList == []:
            break

        diff = mList[0][0] - nList[0][0]

        if diff > 0:
            diffList.append(mList[0][1] - nList[0][1])
            nList.pop(0)
            mList[0][0] = diff

        elif diff < 0:
            diffList.append(mList[0][1] - nList[0][1])
            mList.pop(0)
            nList[0][0] = -diff

        else:
            diffList.append(mList[0][1] - nList[0][1])
            mList.pop(0)
            nList.pop(0)

    if max(diffList) >= 0:
        print(max(diffList))
    else:
        print(0)


if __name__ == "__main__":
    solution1()
