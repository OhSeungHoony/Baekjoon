import sys
from collections import deque

if __name__ == "__main__":
    f, s, g, u, d = map(int, sys.stdin.readline().split())  # 총 층수, 현재층, 목적층, 위, 아래
    board = [-1]*(f+1)
    board[s] = 0
    queue = deque()
    queue.append((s, 0))
    d = [u, -d]

    while queue:
        s, c = queue.popleft()
        for i in range(2):
            n = s + d[i]
            if 0<n<=f and board[n] == -1:
                board[n] = c + 1
                queue.append((n, c+1))

    if board[g] != -1:
        print(board[g])
    else:
        print("use the stairs")