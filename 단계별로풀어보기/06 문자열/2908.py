a, b = map(str, input().split())

new_a = ''
new_b = ''

for i in range(3):
    new_a += a[2-i]
    new_b += b[2-i]

print(max(int(new_a), int(new_b)))
