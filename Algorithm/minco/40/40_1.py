def gka(y,x):
    global result
    result.append([y,x])
    if y==0 and x==0:
        return
    if y-1>0 and x-1>0:
        a=li[y-1][x]
        b=li[y][x-1]
        if a<b:
            y=y-1
        else:
            x=x-1
    elif y-1>=0 and x-1<0:
        y=y-1
        x=x
    else:
        y=y
        x=x-1
    gka(y,x)


arr=[list(map(int,input().split())) for _ in range(4)]
li=[[0]*4 for _ in range(4)]
for i in range(1,4):
    li[i][0]=li[i-1][0]+arr[i][0]
    li[0][i]=li[0][i-1]+arr[0][i]

for i in range(1,4):
    for j in range(1,4):
        li[i][j]=min(li[i][j-1],li[i-1][j])+arr[i][j]

result=[]
gka(3,3)
for i in result[::-1]:
    print(f'{i[0]},{i[1]}')