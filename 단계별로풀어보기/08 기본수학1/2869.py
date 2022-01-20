a, b, v = map(int, input().split())
"""시간초과
if a==v:
  print(1)
else:
  i=2
  while True:
    if (a-b)*(i-1)+a >= v:
      print(i)
      break
    else:
      i += 1
"""
i = (v-b)/(a-b)
if i%1==0:
    print(int(i))
else:
    print(int(i)+1)