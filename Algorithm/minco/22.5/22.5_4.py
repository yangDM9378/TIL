a,b=map(str,input().split())
arr=[[[0]*3 for _ in range(2)] for _ in range(3)]
for k in range(3):
    for i in range(2):
        for j in range(3):
            if i==0:
                arr[k][i][j]=a
            else:
                arr[k][i][j]=b
            print(arr[k][i][j], end=' ')
        print()
    print()