arr=[[3,5,4,1],[1,1,2,3],[6,7,1,2]]
z=list(map(int, input().split()))

def abc(a):
    k=z.index(a)
    return z[(k+1)%4]


for i in range(3):
    for j in range(4):
        if arr[i][j] in z:
            arr[i][j]=abc(arr[i][j])
        print(arr[i][j], end=' ')
    print()
