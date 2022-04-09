allnum = set(range(1, 10000))
oknum = set()
for i in allnum:
    for j in str(i):
        i += int(j)
    oknum.add(i)
selfnum = sorted(allnum - oknum)
for num in selfnum:
    print(num)