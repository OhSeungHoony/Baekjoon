import sys

if __name__ == "__main__":
    n = sys.stdin.readline()
    arr = []
    for num in range(len(n)):
        arr.append(n[num])
    arr.sort(reverse=True)
    for num in arr:
        print(num, end="")
