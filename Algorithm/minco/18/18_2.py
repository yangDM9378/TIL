arr=[list(map(int, input().split())) for i in range(3)]
z_li=[0]*9
for i in range(3):
    for j in range(3):
        z_li[arr[i][j]-1]+=1
li=[]
for k in range(len(z_li)):
    if z_li[k]==0:
        li.append(k)

for z in li:
    print(z+1, end=' ')