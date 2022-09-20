from collections import deque
def bfs(arr):
    global Max
    q=deque()
    for i in li:
        q.append(i)
    while q:
        node=q.popleft()
        nowy,nowx,level=node[0], node[1],node[2]
        if Max<level:
            Max=level
        diry=[0,0,-1,1,-1,-1,1,1]
        dirx=[-1,1,0,0,1,-1,-1,1]
        for k in range(8):
            dy=diry[k]+nowy
            dx=dirx[k]+nowx
            if dx<0 or dy<0 or dx>4 or dy>3:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==0:
                used[dy][dx]=1
                arr[dy][dx]=level+1
                q.append([dy,dx,level+1])



arr=[list(map(int, input().split())) for _ in range(4)]
li=[]
used = [[0] * 5 for _ in range(4)]
for i in range(4):
    for j in range(5):
        if arr[i][j]==1:
            li.append([i,j,0])
            used[i][j]=1
Max=-1
bfs(arr)
print(Max)