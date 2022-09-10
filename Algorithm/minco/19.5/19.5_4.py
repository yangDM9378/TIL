arr=[[0]*4 for _ in range(4)]
for _ in range(3):
    a,b =map(str, input().split())
    if a=='G':
        for i in range(4):
            arr[int(b)][i]=1
    else:
        for i in range(4):
            arr[i][int(b)]=1

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()