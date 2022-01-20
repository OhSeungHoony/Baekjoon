s = str(input())
ans = ''
for abc in range(ord('a'), ord('z')+1):
    if chr(abc) in s:
        ans = s.index(chr(abc))
    else:
        ans = -1
    print(ans, end=' ')