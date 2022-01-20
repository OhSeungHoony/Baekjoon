n = int(input())
cnt = 1
if n==1:
    print(1)
else:
    while n>1:
        n = n - cnt*6
        cnt += 1
    print(cnt)