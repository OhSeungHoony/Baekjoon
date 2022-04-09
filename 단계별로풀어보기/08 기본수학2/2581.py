import sys

def solution(m ,n):
    number = []
    for i in range(m, n+1):
        if i==1:
            pass
        elif i==2:
            number.append(i)
        else:
            for j in range(2, i):
                if i%j==0:
                    break
                elif j==i-1:
                    number.append(i)
    if len(number)==0:
        print(-1)
    else:
        print(sum(number))
        print(min(number))

if __name__ == "__main__":
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    solution(m, n)