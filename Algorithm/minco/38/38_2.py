def bfs(y,x):
    global cnt
    q=deque()
    q.append([y,x])
    while q:
        node=q.popleft()
        nowy,nowx=node[0],node[1]
        diry=[0,0,-1,1]
        dirx=[1,-1,0,0]
        for i in range(4):
            dy=diry[i]+nowy
            dx=dirx[i]+nowx
            if dy<0 or dx<0 or dy>3 or dx>8:continue
            if arr[dy][dx]!=arr[y][x] or used[dy][dx]==1:continue
            cnt+=1
            used[dy][dx]=1
            q.append([dy,dx])


from collections import deque
arr=[list(map(int, input().split())) for _ in range(4)]
used=[[0]*9 for _ in range(4)]
li=[]
for i in range(4):
    for j in range(9):
        if used[i][j]==0:
            cnt=1
            used[i][j]=1
            bfs(i,j)
            li.append([cnt,arr[i][j]])
li.sort()
print(li[-1][0]*li[-1][1])