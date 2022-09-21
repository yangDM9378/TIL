def bfs(y,x,mark):
    global li
    q=deque()
    q.append([y,x,0,'C'])
    while q:
        node=q.popleft()
        nowy,nowx,level,k=node[0],node[1],node[2],node[3]
        li.append(node)
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>7 or dx>8:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==mark:
                used[dy][dx]=1
                q.append([dy,dx,level,'C'])

def bfs_2():
    q=deque()
    q=li[:]
    while q:
        node=q.pop(0)
        nowy,nowx,level,k=node[0],node[1],node[2],node[3]
        if k == '#':
            return level-1
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>7 or dx>8:continue
            if used[dy][dx]==1:continue
            used[dy][dx]=1
            q.append([dy,dx,level+1,arr[dy][dx]])


from collections import deque
arr=[list(input()) for _ in range(8)]
used=[[0]*9 for _ in range(8)]
used[7][0]=1
li=[]
bfs(7,0,'#')
print(bfs_2())