from collections import deque
def bfs(y,x,ey,ex):
    q=deque()
    q.append([y,x,0])
    while q:
        node=q.popleft()
        nowy=node[0]
        nowx=node[1]
        level=node[2]
        if nowy==ey and nowx==ex:
            return level
        diry=[0,0,-1,1]
        dirx=[-1,1,0,0]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>3 or dx>3:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==0:
                used[dy][dx]=1
                q.append([dy,dx,level+1])


arr=[[0,0,0,0],[1,1,0,1],[0,0,0,0],[1,0,1,0]]
used=[[0]*4 for _ in range(4)]

y,x= map(int,input().split())
used[y][x]=1
ey,ex=map(int, input().split())
result=bfs(y,x,ey,ex)
print(f'{result}회')
