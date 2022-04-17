import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split(' '))
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    t_range = []
    for _ in range(m):
        t_range.append(list(map(int, sys.stdin.readline().split(' '))))
    D = [0]*n
    D[0] = numbers[0]
    for i in range(1, n):
        D[i] = D[i-1] + numbers[i]
    for test in t_range:
        a = test[0]
        b = test[1]
        if a == 1:
            print(D[b-1])
        else:
            print(D[b-1] - D[a-2])