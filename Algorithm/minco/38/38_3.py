def pattern(y,x,n,k):
    diry = [0, 0, -1, 1]
    dirx = [-1, 1, 0, 0]
    for i in range(1, n+1):
        for j in range(4):
            dy = diry[j] * i + y
            dx = dirx[j] * i + x
            if dy < 0 or dx < 0 or dy > 6 or dx > 6: continue
            if arr[dy][dx]==k:
                return 1
    return 0


def bfs(y,x):
    global flag
    q=deque()
    q.append([y,x,arr[y][x]])
    while q:
        node=q.popleft()
        nowy,nowx,k=node[0],node[1],node[2]
        if k=='1':
            flag+=pattern(nowy,nowx,2,k)
        elif k=='2':
            flag+=pattern(nowy,nowx,3,k)
        diry = [0, 0, -1, 1]
        dirx = [-1, 1, 0, 0]
        for j in range(4):
            dy = diry[j]+nowy
            dx = dirx[j]+nowx
            if dy < 0 or dx < 0 or dy > 6 or dx > 6: continue
            if used[dy][dx]==1:continue
            used[dy][dx]=1
            q.append([dy,dx,arr[dy][dx]])



from collections import deque
arr=[list(input()) for _ in range(7)]
used=[[0]*7 for _ in range(7)]
flag=0
used[0][0]=1
bfs(0,0)
if flag==0:
    print('pass')
else:
    print('fail')