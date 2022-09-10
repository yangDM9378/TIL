arr=[list(map(int, input().split())) for _ in range(3)]
z=[[0]*4 for _ in range(4)]

for i in range(3):
    for j in range(3):
        z[i][j]=arr[i][j]


for i in range(3):
    sum = 0
    for j in range(3):
        sum+=arr[i][j]
    z[i][j+1]=sum

for j in range(3):
    sum = 0
    for i in range(3):
        sum+=arr[i][j]
    z[i+1][j]=sum

sum=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum+=arr[i][j]
z[i+1][j+1]=sum
for i in range(4):
    for j in range(4):
        print(z[i][j], end=' ')
    print()