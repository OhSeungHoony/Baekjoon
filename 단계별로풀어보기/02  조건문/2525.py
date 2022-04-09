def clock(h, m, time):
    m += time
    extra_h = 0
    if m>59:
        extra_h = m // 60
        m = m % 60
    h += extra_h
    h = h % 24
    return f"{h} {m}"
h, m = map(int, input().split())
time = int(input())
finish_time = clock(h=h, m=m, time=time)
print(finish_time)