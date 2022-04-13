n = int(input())
count = 0

while n > 0:
    if n%5 == 0:
        count += n//5
        break        
    count += 1
    n -= 3
    
    if 0 > n:
        count = -1
        
print(count)