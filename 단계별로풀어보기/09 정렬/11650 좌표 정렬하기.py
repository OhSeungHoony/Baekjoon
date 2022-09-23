if __name__ == "__main__":
    n = int(input())
    dot = []
    for _ in range(n):
        dot.append(list(map(int, input().split())))

    dot.sort(key=lambda x: (x[0], x[1]))

    for i in range(n):
        print(dot[i][0], dot[i][1])
