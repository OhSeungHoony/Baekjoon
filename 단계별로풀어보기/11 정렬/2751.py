import sys

def sort_num(numbers):
    numbers.sort()
    for num in numbers:
        print(num)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = []
    for _ in range(n):
        num = int(sys.stdin.readline())
        numbers.append(num)
    sort_num(numbers)