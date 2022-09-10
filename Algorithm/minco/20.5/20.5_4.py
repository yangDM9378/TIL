arr1=[list(map(int, input().split())) for _ in range(4)]
a=input()
arr2=[list(map(int, input().split())) for _ in range(4)]
z=[[0]*4 for _ in range(4)]

flag=0
for i in range(4):
    for j in range(4):
        z[i][j]+=arr1[i][j]
        z[i][j]+=arr2[i][j]
        if z[i][j]==2:
            flag=1

if flag==1:
    print('걸리다',end='')
else:
    print('걸리지않는다',end='')