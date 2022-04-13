numList = []
namList = []
for i in range(10):
    numList.append(int(input()))
for num in numList:
    nam = num % 42
    if nam in namList:
        pass
    else:
        namList.append(nam)
print(len(namList))
    
