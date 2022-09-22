def bfs(y,x,k):
    q=deque()
    q.append([y,x,0])
    used = [[0] * m for _ in range(n)]
    used[y][x]=1
    while q:
        node=q.popleft()
        nowy, nowx, level=node[0], node[1], node[2]
        if arr[nowy][nowx]==k:
            return nowy,nowx,level
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]!='#':
                used[dy][dx]=1
                q.append([dy,dx,level+1])


from collections import deque
n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]
li=[0]*4
y=0
x=0
cnt=0
for i in range(4):
    y,x,level=bfs(y,x,str(i+1))
    cnt+=level
print(f'{cnt}회')

