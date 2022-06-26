N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    K=[]
    for j in range(M):
        K.append(A[i][j]+B[i][j])
    for o in range(M):
        print(K[o],end=' ')
    print('')
