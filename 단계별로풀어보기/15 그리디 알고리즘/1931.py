import sys

def greedy(time_stamp):
    start = 0
    cnt = 0
    for time in time_stamp:
        if time[0] >= start:
            start = time[1]
            cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    time_stamp = []
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().split())
        time_stamp.append((start, end))
    time_stamp = sorted(time_stamp, key=lambda a:a[0])
    time_stamp = sorted(time_stamp, key=lambda a:a[1])
    print(greedy(time_stamp))
