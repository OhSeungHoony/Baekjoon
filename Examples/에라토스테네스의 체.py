"""
    에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

    이 알고리즘은 다음과 같다.

    1. 2부터 N까지 모든 정수를 적는다.
    2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
    3. P의 배수를 크기 순서대로 지운다.
    4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

    N이 주어졌을 때 N 이하의 소수를 출력하시오.
"""
if __name__ == "__main__":
    n = int(input())
    board = [False, False] + [True for _ in range(n-1)]
    prime = []
    for i in range(n+1):
        if board[i] == False:
            continue

        if board[i] == True:
            prime.append(i)

            for j in range(i*2, n+1, i):
                board[j] = False

    for p in prime:
        if p == prime[-1]:
            print(p, end="")
        else:
            print(p, end=", ")