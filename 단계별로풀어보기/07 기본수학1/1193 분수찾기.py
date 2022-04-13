n = int(input())
i=0
n = n+1
while n>1:
    ncnt = n-1
    n = n-i
    i += 1
cnt = i-1
if cnt%2 == 0:
    print(f'{ncnt}/{cnt-ncnt+1}')
else:
    print(f'{cnt-ncnt+1}/{ncnt}')