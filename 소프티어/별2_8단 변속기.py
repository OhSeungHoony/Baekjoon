import sys

def solution1():
    num_list = list(map(int, sys.stdin.readline().split()))
    if num_list == sorted(num_list):
        print('ascending')
    elif num_list == sorted(num_list, reverse=True):
        print('descending')
    else:
        print('mixed')


if __name__ == "__main__":
    solution1()

