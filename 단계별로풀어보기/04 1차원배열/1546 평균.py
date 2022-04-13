def getAvg(arr):
    return sum(arr)/len(arr)

n = int(input())
scoreList = list(map(int, input().split()))

newAvg = getAvg(scoreList)/max(scoreList)*100

print(newAvg)
