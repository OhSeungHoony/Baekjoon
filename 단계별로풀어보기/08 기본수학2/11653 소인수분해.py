import sys

def solution(n):
    number = []
    t = n
    i = 2
    while True:
        if i > n:
            break
        if t % i == 0:
            number.append(i)
            t = t // i
        else:
            i += 1
    number.sort()
    for num in number:
        print(num)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n != 1:
        solution(n)
