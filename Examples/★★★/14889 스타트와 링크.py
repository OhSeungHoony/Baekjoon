n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

team_kind = 1
for i in range(n):
    if i < n//2:
        team_kind = team_kind * (n - i) // (i + 1)
    else:
        break
team_kind = team_kind // 2



score_list = [0 for _ in range(team_kind)]



for i in range(n):
    for j in range(n):
