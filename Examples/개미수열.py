"""
    소설 개미에 나온 수열.
    1, 11, 12, 1121, 122111, 112213,,,,
    이런 식으로 이전 값의 숫자의 갯수를 반환하는 수열.
    n번째를 구하는 코드를 작성하시오.
"""

n=int(input())-1
a='1'
for i in range(n):
    count=0
    new_start=a[0]
    new=''
    for j in range(len(a)):
        if a[j]==new_start:
            count+=1
        else:
            new=new+new_start+str(count)
            new_start=a[j]
            count=1

    a=new+new_start+str(count)

print(a)