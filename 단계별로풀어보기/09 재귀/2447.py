def Stars(n):
    global page

    if n == 3:
        page[0][:3] = page[2][:3] = [1, 1, 1]
        page[1][:3] = [1, 0, 1]
        return

    a = n//3
    Stars(a)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                page[a*i+k][a*j:a*(j+1)] = page[k][:a]

n = int(input())

page = [[0 for i in range(n)] for i in range(n)]

Stars(n)

for i in page:
    for j in i :
        if j:
            print("*", end="")
        else:
            print(" ", end="")
    print()