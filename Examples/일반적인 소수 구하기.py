"""
    일반적인 방법으로 n 이하의 소수를 출력하시오.
"""

if __name__ == "__main__":
    n = int(input())

    prime = []
    for i in range(2, n+1):
        for j in range(2, i+1):
            if i == j:
                prime.append(j)
            elif i % j == 0:
                break

    for p in prime:
        if p == prime[-1]:
            print(p, end="")
        else:
            print(p, end=", ")