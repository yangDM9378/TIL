from collections import deque

n=int(input())
ay,ax,by,bx=map(int, input().split())
arr=[[0]*n for _ in range(n)]
q=deque()
q.append([ay,ax,1])
q.append([by,bx,1])
arr[ay][ax]=1
arr[by][bx]=1
while q:
    node=q.popleft()
    y,x, level= node[0], node[1],node[2]
    diry=[-1,1,0,0]
    dirx=[0,0,-1,1]
    for i in range(4):
        dy=diry[i]+y
        dx=dirx[i]+x
        if dy<0 or dy>n-1 or dx<0 or dx>n-1:continue
        if arr[dy][dx]==0:
            arr[dy][dx]=level+1
            q.append([dy,dx,level+1])
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()