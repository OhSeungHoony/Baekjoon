import sys
from collections import deque

def bfs(x, y, ans):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
    ans += 1
    return ans

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for _ in range(t):
        m, n, k = map(int, sys.stdin.readline().split())
        board = [[0]*m for _ in range(n)]
        for _ in range(k):
            b, a = map(int, sys.stdin.readline().split())
            board[a][b] = 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    ans = bfs(i, j, ans)
        print(ans)