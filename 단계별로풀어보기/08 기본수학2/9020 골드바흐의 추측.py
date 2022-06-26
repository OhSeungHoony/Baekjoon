if __name__ == "__main__":
    t = int(input())
    numbers = []
    for _ in range(t):
        num = int(input())
        numbers.append(num)

    n = max(numbers)
    board = [False, False] + [True for _ in range(n - 1)]
    prime = []
    for i in range(n + 1):
        if board[i] == False:
            continue

        if board[i] == True:
            prime.append(i)

            for j in range(i * 2, n + 1, i):
                board[j] = False

    for num in numbers:
        for p in prime:
            ex_p = num - p
            if ex_p in prime:
                x, y = p, ex_p
            if p >= num//2:
                break
        print(min(x, y), max(x, y))
