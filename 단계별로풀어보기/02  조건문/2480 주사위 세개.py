import sys

def solution(numbers):
    numbers.sort(reverse=True)
    if numbers[0] == numbers[2]:
        print(numbers[0]*1000 + 10000)
    elif numbers[0] == numbers[1] and numbers[1] != numbers[2]:
        print(numbers[0]*100 + 1000)
    elif numbers[0] != numbers[1] and numbers[1] == numbers[2]:
        print(numbers[1]*100 + 1000)
    else:
        print(numbers[0]*100)

if __name__ == "__main__":
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    solution(numbers)