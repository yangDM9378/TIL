from collections import deque
def bfs(y,x):
    global Max
    q=deque()
    q.append([y,x,0])
    while q:
        node=q.popleft()
        nowy, nowx,level=node[0],node[1],node[2]
        if level>Max:
            Max=level
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy = nowy + diry[i]
            dx = nowx + dirx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==0:
                used[dy][dx]=1
                arr[dy][dx]=level+1
                q.append([dy,dx,level+1])






n,m=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(m)]
used=[[0]*n for _ in range(m)]
y,x=map(int, input().split())
used[y][x]=1
Max=-111
bfs(y,x)
print(Max)
