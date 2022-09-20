def bfs(y,x):
    global cnt
    q=deque()
    q.append([y,x])
    while q:
        node=q.popleft()
        nowy, nowx=node[0], node[1]
        diry=[0,0,-1,1]
        dirx=[-1,1,0,0]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>3 or dx>5:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==1:continue
            if arr[dy][dx]==2:
                cnt+=1
            used[dy][dx]=1
            q.append([dy,dx])

from collections import deque
arr=[list(map(int,input().split())) for i in range(4)]
used=[[0]*6 for _ in range(4)]
used[0][0]=1
cnt=0
bfs(0,0)
print(cnt)