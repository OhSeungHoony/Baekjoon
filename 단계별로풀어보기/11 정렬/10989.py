import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = [0]*10000
    for i in range(n):
        num = int(sys.stdin.readline())
        numbers[num-1] += 1
    for i in range(10000):
        if numbers[i] != 0:
            for j in range(numbers[i]):
                print(i+1)
