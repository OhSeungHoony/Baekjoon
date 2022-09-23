def solution(money):
    h = len(money)
    if h == 3:
        return max(money)
    # 첫번째 집을 털었다면 마지막 집은 털 수 없다.

    # 첫번째 집 턴 경우
    dp1 = [0] * (h - 1)
    dp1[0] = money[0]
    dp1[1] = money[1]
    for i in range(2, h - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
    an1 = max(dp1)
    # 첫번째 집 안 턴 경우
    dp2 = [0] * h
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, h):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])
    an2 = max(dp2)

    return max(an1, an2)