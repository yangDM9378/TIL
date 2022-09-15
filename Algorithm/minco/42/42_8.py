def dfs(y,x):
    global ret
    if y==(n-1) and x==(n-1):
        ret=1
        return

    for i in range(4):
        dy=diry[i]+y
        dx=dirx[i]+x
        if dx<0 or dy<0 or dx>n-1 or dy>n-1:continue
        if arr[dy][dx]==1 or used[dy][dx]==1:continue
        used[dy][dx]=1
        dfs(dy,dx)
        used[dy][dx]=0



n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
ret=0
used=[[0]*n for _ in range(n)]
diry=[-1,1,0,0]
dirx=[0,0,-1,1]
dfs(0,0)
if ret==1:
    print('가능')
else:
    print('불가능')