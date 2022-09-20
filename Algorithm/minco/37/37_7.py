from collections import deque
def whkvy(arr, word):
    for i in range(N):
        for j in range(M):
            if arr[i][j]==word:
                return i,j

def bfs(y,x,ey,ex):
    used=[[0]*M for _ in range(N)]
    used[y][x]=1
    q=deque()
    q.append([y,x,0])
    while q:
        node=q.popleft()
        nowy,nowx,level=node[0],node[1],node[2]
        if nowy==ey and nowx==ex:
            return level
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>N-1 or dx>M-1:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]=='x':continue
            used[dy][dx]=1
            q.append([dy,dx,level+1])

N, M = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(N)]
s_y,s_x=whkvy(arr,'S')
c_y,c_x=whkvy(arr,'C')
d_y,d_x=whkvy(arr,'D')
print(bfs(s_y,s_x,c_y,c_x)+bfs(c_y,c_x,d_y,d_x))