n = int(input())
result_list = []

for i in range(n):
    ox_list = input()
    current_score = 0
    combo_score = 0
    for ox in ox_list:
        if ox == 'O':
            combo_score += 1
        else:
            combo_score = 0
        current_score += combo_score
    result_list.append(current_score)

for i in range(n):
    print(result_list[i])
