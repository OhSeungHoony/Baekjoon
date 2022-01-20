# import sys
# input = sys.stdin.readline
c = int(input())
result = 0
result_list=[]
for i in range(c):
    testCase = list(map(int, input().split()))
    num = []
    for j in range(1, testCase[0]+1):
        num.append(testCase[j])
    numAvg = sum(num)/testCase[0]
    cnt = 0
    for n in num:
        if n > numAvg:
            cnt += 1
    result = round(cnt / testCase[0]*100, 3)
    result_list.append("{:.3f}%".format(result))
for ans in result_list:
    print(ans)