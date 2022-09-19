import sys
# 오는 순서가 아니므로 대기시간이 없어, 단순히 적게 걸리는 사람부터 세워야 최적. -> 그리디
def solution(n, t_list):
    t_list.sort()
    ans = 0
    for i in range(n):
        ans += t_list[i] * (n - i)
    print(ans)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    t_list = list(map(int, sys.stdin.readline().split(' ')))

    solution(n, t_list)
