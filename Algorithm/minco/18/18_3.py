arr=[
    [1, 3, 3, 5, 1],
    [3, 6, 2, 4, 2],
    [1, 9, 2, 6, 5]
    ]

z_li=[0]*9
for i in range(3):
    for j in range(5):
        z_li[arr[i][j]-1]+=1

a=int(input())
for k in range(len(z_li)):
    if z_li[k]==a:
        print(k+1, end=' ')