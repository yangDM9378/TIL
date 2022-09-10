arr=[[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,1,2,0,2,1,0],[0,0,1,2,1,0,0],[0,0,2,1,0,1,0],[0,1,1,0,0,0,0],[0,0,0,0,0,0,0]]
diry=[0,0,-1,1]
dirx=[1,-1,0,0]

def pattern(y,x):
    cnt=0
    for i in range(4):
        dy=diry[i]+y
        dx=dirx[i]+x
        if dy<0 or dy>6 or dx<0 or dx>6:
            break
        else:
            if arr[dy][dx]==1:
                cnt+=1
    return cnt

y,x=map(int,input().split())
arr[y][x]=1

result=0
for p in range(7):
    for z in range(7):
        if arr[p][z]==2:
            rat=pattern(p,z)
            if rat==4:
                result+=1
print(result)