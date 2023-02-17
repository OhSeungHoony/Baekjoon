import sys
from collections import deque

def bfs(queue, n, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num = 0
    while queue:
        x, y = queue.popleft()
        num += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == "1":
                queue.append([nx, ny])
                board[nx][ny] = "0"
    return num

def solution1():
    n = int(sys.stdin.readline())
    board = [list(sys.stdin.readline()) for _ in range(n)]

    queue = deque()
    cnt = 0
    # print(board)
    num_list = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "1":
                board[row][col] = 0
                queue.append([row, col])
                num_list.append(bfs(queue, n, board))
                cnt += 1
    print(cnt)
    num_list.sort()
    for num in num_list:
        print(num)


if __name__ == "__main__":
    solution1()
