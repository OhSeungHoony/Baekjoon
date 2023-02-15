from itertools import combinations
import sys

a = int(sys.stdin.readline())
list1 = [1, 2, 3, 4]

for item in combinations(list1, 2):
    print(item)