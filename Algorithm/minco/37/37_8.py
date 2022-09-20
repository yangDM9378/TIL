def bfs(y,x):
    q=deque()
    q.append([y,x])
    while q:
        node=q.popleft()
        nowy,nowx=node[0], node[1]
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=diry[i]+nowy
            dx=dirx[i]+nowx
            if dy<0 or dx<0 or dy>N-1 or dx>M-1:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==1:
                used[dy][dx]=1
                q.append([dy,dx])

from collections import deque
N,M=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(N)]
used=[[0]*M for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and used[i][j]!=1:
            used[i][j]=1
            cnt+=1
            bfs(i,j)
print(cnt)