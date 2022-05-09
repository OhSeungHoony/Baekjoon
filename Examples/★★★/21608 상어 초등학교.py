import sys

def score(dic, board, move, n):
    score_list = [0, 1, 10, 100, 1000]
    happy_list = []
    for i in range(n):
        for j in range(n):
            happy = 0
            for dx, dy in move:
                tx = i + dx
                ty = j + dy
                if tx < 0 or tx >= n or ty < 0 or ty >= n:
                    continue
                if board[tx][ty] in dic.get(board[i][j]):  # 만약 인접칸의 번호가 좋아하는 번호라면
                    happy += 1
            happy_list.append(score_list[happy])
    return sum(happy_list)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dic = dict()
    student_num = [0] * (n * n)
    board = [[0]*n for _ in range(n)]
    move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    for i in range(n*n):
        info = list(map(int, sys.stdin.readline().split()))
        dic[info[0]] = info[1:]
        student_num[i] = info[0]
    # 빈칸수 같으면 우선 위로, 그래도 같으면 왼쪽으로
    # 첫 번째 학생은 칸수에 상관없이 (1,1)
    board[1][1] = student_num[0]
    for num in student_num[1:]:
        preDesk = [] # 만족도 가장 높은 자리 리스트
        maxHappy = 0  # 가장 높은 만족도
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0:
                    continue
                happy = 0
                empty = 0
                for dx, dy in move:
                    tx = i + dx
                    ty = j + dy
                    if tx<0 or tx>=n or ty<0 or ty>=n:
                        continue
                    if board[tx][ty] == 0: # 만약 인접칸이 비어있다면
                        empty += 1
                    if board[tx][ty] in dic.get(num): # 만약 인접칸의 번호가 좋아하는 번호라면
                        happy += 1
                if happy > maxHappy:
                    maxHappy = happy
                    preDesk = []
                    preDesk.append((i, j, empty))
                if happy == maxHappy:
                    preDesk.append((i, j, empty))

        preDesk.sort(key=lambda i: (-i[2], i[0], i[1]))  # 빈칸우선, 위쪽, 왼쪽
        x, y, empty = preDesk[0]
        board[x][y] = num
    # 자리 배치 완료.

    # 점수 계산 시작.
    print(score(dic, board, move, n))