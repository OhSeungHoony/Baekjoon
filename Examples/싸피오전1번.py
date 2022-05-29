test_case = int(input())
for c in range(test_case):
    n = int(input())
    round_list = [0 for _ in range(n)]
    num_list = list(map(int, input().split()))
    for i in range(n):
        round_list[i] = num_list[i]
    round_list.sort()

    cnt = 0
    for i in range(n):
        if round_list[i] == num_list[i]:
            pass
        else:
            cnt += 1
    if cnt == 0:
        print(f"#{c+1} 0")
    else:
        cnt = 0
        while True:
            for i in range(0, n, 2):
                if i+1 < n:
                    if num_list[i] > num_list[i+1]:
                        tmp = num_list[i]
                        num_list[i] = num_list[i+1]
                        num_list[i+1] = tmp
            for i in range(1, n, 2):
                if i+1 < n:
                    if num_list[i] > num_list[i+1]:
                        tmp = num_list[i]
                        num_list[i] = num_list[i+1]
                        num_list[i+1] = tmp
            cnt += 1
            t = 0
            for i in range(n):
                if round_list[i] == num_list[i]:
                    pass
                else:
                    t += 1
            if t == 0:
                break

        print(f"#{c+1} {cnt}")

# print("#%d" % test_case)