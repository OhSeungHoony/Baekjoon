n = int(input())
num = str(input())
numList = list(map(int, num))
sumNum = 0
for i in range(n):
    sumNum += numList[i]
print(sumNum)