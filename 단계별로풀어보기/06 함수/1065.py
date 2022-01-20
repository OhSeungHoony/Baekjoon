n = int(input())
cnt = 0
for i in range(1, n+1):
    if i<100:
        cnt += 1
    else:
        numList = list(map(int, str(i)))
        if numList[1]-numList[0] == numList[2]-numList[1]:
            cnt += 1
print(cnt)