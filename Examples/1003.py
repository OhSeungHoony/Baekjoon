t = int(input())

cnt_0 = [1, 0, 1]
cnt_1 = [0, 1, 1]

def fib(n):
    if len(cnt_0) <= n:
        for i in range(len(cnt_0), n+1):
            cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
            cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    print(cnt_0[n], cnt_1[n])

for _ in range(t):
    n = int(input())
    fib(n)
