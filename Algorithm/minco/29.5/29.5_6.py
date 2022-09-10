arr=[[3,2,5,3],
     [7,6,1,6],
     [4,9,2,7]]
z=[[0]*4 for _ in range(3)]

a,b,c,d=map(int, input().split())

for i in range(3):
    z[(i + a) % 3][0] = arr[i][0]
for i in range(3):
    z[(i + b) % 3][1] = arr[i][1]
for i in range(3):
    z[(i + a) % 3][2] = arr[i][2]
for i in range(3):
    z[(i + b) % 3][3] = arr[i][3]

for k in range(3):
    for p in range(4):
        print(z[k][p], end='')
    print()
