inf=(int)(21e8)
arr=[
    [0,5,inf,8],
    [7,0,9,inf],
    [2,inf,0,4],
    [inf,inf,3,0]
]
for k in range(4):
    for s in range(4):
        for d in range(4):
            if arr[s][d]>arr[s][k]+arr[k][d]:
                arr[s][d]=arr[s][k]+arr[k][d]

for i in range(4):
    for j in range(4):
        print(arr[i][j],end=' ')
    print()