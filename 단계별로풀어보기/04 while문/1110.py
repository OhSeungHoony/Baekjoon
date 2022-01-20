n = int(input())
m = n
cnt = 0

while True:
    newN = m//10 + m%10
    m = (m%10)*10 + newN%10
    cnt += 1
    if m==n:
        break
print(cnt)
