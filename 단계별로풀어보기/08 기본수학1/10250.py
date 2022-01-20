t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    x = n//h
    y = n%h
    if y==0:
        if x < 10:
            print(f'{h}0{x}')
        else:
            print(f'{h}{x}')
    else:
        if x+1 < 10:
            print(f'{y}0{x+1}')
        else:
            print(f'{y}{x+1}')