han=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
arr=list(map(int, input().split()))
z=[[0]*4 for _ in range(4)]

for j in range(4):
    for i in range(4):
        for k in range(4):
            if han[j][i] == arr[k]:
                z[j][i]=k+1
for i in range(4):
    for j in range(4):
        print(z[i][j], end=' ')
    print()