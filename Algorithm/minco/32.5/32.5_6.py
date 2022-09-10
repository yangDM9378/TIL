N,K=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]
z=[[0]*N for _ in range(N)]
q=0
while q<(K%4):
    z=[[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            z[i][j] = arr[N-1-j][i]
    arr=z[:]
    q+=1
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()