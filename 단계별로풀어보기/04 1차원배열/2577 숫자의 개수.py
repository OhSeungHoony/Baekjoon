a = int(input())
b = int(input())
c = int(input())

gob = a*b*c
goblist = list(str(gob))

for i in range(10):
    print(goblist.count(str(i)))
