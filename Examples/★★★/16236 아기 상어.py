import sys
import heapq as hq

def find_shark(n, fish):
    start = (0, 0)
    for i in range(n):
        for j in range(n):
            if fish[i][j] == 9:
                start = (i, j)
    return start

def bfs(n, fish, start, level):
    queue1 = [] # 큐
    visited = [([False]*n) for _ in range(n)]
    dist = 0    # 거리
    feed = 0    # 먹은 수
    ans = 0     # 총 이동 횟수
    hq.heappush(queue1, (dist, start[0], start[1])) # 거리, 행, 열
    fish[start[0]][start[1]] = 0    # 상어가 처음 있던 위치를 0으로 바꿈

    dx = [-1, 0, 0, 1]  # 상, 좌, 우, 하
    dy = [0, -1, 1, 0]

    while queue1:
        dist, row, col = hq.heappop(queue1)
        if 0 < fish[row][col] < level:
            queue1 = []
            fish[row][col] = 0
            visited = [([False] * n) for _ in range(n)]
            ans += dist
            dist = 0
            feed += 1
            if feed == level:
                level += 1
                feed = 0
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if visited[x][y] == False:
                    if fish[x][y] <= level:
                        visited[x][y] = True
                        hq.heappush(queue1, (dist+1, x, y))
    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    fish = []
    for _ in range(n):
        fish.append(list(map(int, sys.stdin.readline().split())))
    start = find_shark(n, fish) # 상어 시작 지점
    level = 2   # 처음 레벨
    print(bfs(n, fish, start, level))