arr=[[3,5,9],[4,2,1],[1,1,5]]
li=[]
for _ in range(3):
    k=list(map(int,input().split()))
    li.append(k)

k=0
for i in range(3):
    for j in range(3):
        if li[i][j]==1:
            k+=arr[i][j]
print(k)