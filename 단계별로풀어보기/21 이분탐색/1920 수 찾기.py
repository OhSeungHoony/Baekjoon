def binarySearch(A, target, st, en):
    if st > en:
        return 0
    mid = (st + en) // 2
    if target == A[mid]:
        return 1
    elif target > A[mid]:
        return binarySearch(A, target, mid+1, en)
    else:
        return binarySearch(A, target, st, mid-1)

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split(' ')))
    m = int(input())
    B = list(map(int, input().split(' ')))

    A.sort()

    for target in B:
        st = 0
        en = n-1
        print(binarySearch(A, target, st, en))
