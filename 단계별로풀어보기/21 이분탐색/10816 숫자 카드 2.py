import sys

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    cnt = {}
    for target in A:
        if target not in cnt:
            cnt[target] = 1
        else:
            cnt[target] += 1

    for target in B:
        st = 0
        en = n-1
        while st <= en:
            mid = (st + en) // 2

            if target == A[mid]:
                break
            elif target > A[mid]:
                st = mid + 1
            else:
                en = mid - 1
        if target == A[mid]:
            print(cnt[target], end=" ")
        else:
            print(0, end=" ")
