a = int(input())
b = input()
for i in range(1, len(b)+1):
    print(a*int(b[len(b)-i]))
print(a*int(b))