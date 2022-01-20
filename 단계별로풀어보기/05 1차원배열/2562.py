num_list=[]
cnt = 0
maxnum = 0
for i in range(9):
    num_list.append(int(input()))
    if num_list[i] > maxnum:
        maxnum = num_list[i]
        cnt = i+1
print(maxnum)
print(cnt)
