import sys
# 이게 왜 그리딘줄 모르겠음
def solution(sik):
    plus = []
    cnt = 0
    for i in sik.split('-'):
        cnt += 1
        numbers = list(map(int, i.split('+')))
        plus.append(sum(numbers))
    ans = 0
    for i in range(cnt):
        if i == 0:
            ans += plus[i]
        else:
            ans -= plus[i]
    print(ans)

if __name__ == "__main__":
    sik = sys.stdin.readline()
    solution(sik)
