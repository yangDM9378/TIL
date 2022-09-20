from collections import deque
# q=deque()
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)
# print(*q)
# q.appendleft(9)
# print(*q)
# x=q.popleft()
# print(x)
# print(*q)

# arr=[[0,1,0,1,0,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# q=deque()
# name=list(input().split())
# answer=[]
# def bfs(st):
#     global answer
#     q=deque()
#     q.append(st)
#     while q:
#         now=q.popleft()
#         answer.append(name[now])
#         for i in range(6):
#             if arr[now][i]==1:
#                 q.append(i)
# bfs(0)
# print(*answer)


# name=['A','B','C','D']
# arr=[[0,1,1,0],[0,0,1,1],[0,1,0,1],[0,0,0,0]]
# answer=[]
# used=[0]*4
#
# def bfs(st):
#     global answer
#     q = deque()
#     q.append(st)
#     while q:
#         now=q.popleft()
#         answer.append(name[now])
#         for i in range(len(name)):
#             if used[i]==1:continue
#             if arr[now][i]==1:
#                 q.append(i)
#                 used[i]=1
# used[1]=1
# bfs(1)
# print(*answer)


# # floodfill 문제 virus 문제
# from collections import deque
# n=int(input()) # map 사이즈 입력
# y,x=map(int,input().split()) # 시작점 입력
# arr=[[0]*n for _ in range(n)]
#
# arr[y][x]=1
# q=deque()
# q.append((y,x,0))
#
# answer=0
# while q:
#     y,x,level=q.popleft()
#     # if y==0 and x==0: answer=level
#     directy=[0,0,1,-1]
#     directx=[1,-1,0,0]
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if 0<=dy<n and 0<=dx<n:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=arr[y][x]+1
#                 q.append((dy,dx,level+1))
#                 # if dy==0 and dx==0:
#                 #     answer=level+1
# for i in arr:
#     print(*i)
# print(answer)

# n=int(input())
# arr=[[0]*n for _ in range(n)]
# y1,x1,y2,x2=map(int, input().split())
# arr[y1][x1]=1
# arr[y2][x2]=1
# q=deque()
# q.append([y1,x1])
# q.append([y2,x2])
#
# while q:
#     now=q.popleft()
#     y,x=now[0],now[1]
#     diry=[0,0,1,-1]
#     dirx=[-1,1,0,0]
#     for i in range(4):
#         dy=y+diry[i]
#         dx=x+dirx[i]
#         if 0<=dx<n and 0<=dy<n:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=arr[y][x]+1
#                 q.append([dy,dx])
# Max=0
# for i in range(n):
#     for j in range(n):
#         if Max<arr[i][j]:
#             Max=max(arr[i][j],Max)
# print(Max-1)

# from collections import deque
# n = int(input()) # 배열 크기입력
# flower = list(map(int, input().split())) # 좌표 입력
# y1, x1 = flower[0], flower[1]
# y2, x2 = flower[2], flower[3]
# flower = [(y1, x1,1), (y2, x2,1)]
# arr = [[0] * n for _ in range(n)]  # 화단 선언
#
# answer=0
#
# def bfs(flower):
#     global n, arr,answer
#     q=deque(flower)
#
#     while q:
#         nowy,nowx,level=q.popleft()
#
#         arr[nowy][nowx]=level
#         answer=level
#
#         directy=[-1,1,0,0]
#         directx=[0,0,-1,1]
#
#         for i in range(4):
#             dy=nowy+directy[i]
#             dx=nowx+directx[i]
#             if not(0<=dy<n and 0<=dx<n):continue # 배열범위
#             if arr[dy][dx]!=0: continue # 이미 꽃이 심어진곳 안됨
#             arr[dy][dx]=arr[nowy][nowx]+1 # 화단에 표시해주기
#             q.append((dy,dx,level+1)) # 큐에 푸쉬하기
#
# bfs(flower)
#
# for row in arr:
#     print(*row,sep="")
# print(answer)


# # 미로찾기문제
# from collections import deque
# arr = [
#     [0,0,0,1,1],
#     [1,0,0,1,0],
#     [1,0,0,0,0],
#     [0,0,0,0,0]
# ]
# dy = [0,0,1,-1]
# dx = [1,-1,0,0]
#
# answer = 0
# def bfs(st_y, st_x, ed_y, ed_x):
#     q = deque()
#     q.append([st_y, st_x, 0])
#     used = [[False]*5 for _ in range(4)]
#     used[st_y][st_x] = True
#     while q:
#         node = q.popleft()
#         yy, xx, level = node[0], node[1], node[2]
#         if yy == ed_y and xx == ed_x:
#             return level
#         for i in range(4):
#             nx = dx[i] + yy
#             ny = dy[i] + xx
#             if not (0<=nx<4 and 0<=ny<5): continue
#             if used[nx][ny] == True: continue
#             if arr[nx][ny] == 1: continue
#             q.append([nx,ny,level+1])
#
# answer += bfs(0,0,3,0)
# answer += bfs(3,0,3,4)
# print(answer)


# # from collections import deque
# # 섬의 넓이
# def whkvy(arr):
#     for i in range(5):
#         for j in range(5):
#             if arr[i][j]==1:
#                 return i,j
# def bfs(y,x):
#     global cnt
#     q=deque()
#     q.append([y,x])
#     while q:
#         node=q.popleft()
#         cnt+=1
#         y,x=node[0],node[1]
#         diry=[1,-1,0,0]
#         dirx=[0,0,-1,1]
#         for i in range(4):
#             dy=diry[i]+y
#             dx=dirx[i]+x
#             if dy<0 or dy>4 or dx<0 or dy>4:continue
#             if used[dy][dx]==1:continue
#             if arr[dy][dx]==0:continue
#             used[dy][dx]=1
#             q.append([dy,dx])
#
# arr=[[0,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]]
# used=[[0]*5 for _ in range(5)]
# y,x=whkvy(arr)
# used[y][x]=1
# cnt=0
# bfs(y,x)
# print(cnt)


# # 섬의 갯수
# def bfs(y,x):
#     global cnt
#     q=deque()
#     q.append([y,x])
#     while q:
#         node=q.popleft()
#         cnt+=1
#         y,x=node[0],node[1]
#         diry=[1,-1,0,0]
#         dirx=[0,0,-1,1]
#         for i in range(4):
#             dy=diry[i]+y
#             dx=dirx[i]+x
#             if dy<0 or dy>4 or dx<0 or dx>4:continue
#             if used[dy][dx]==1:continue
#             if arr[dy][dx]==0:continue
#             used[dy][dx]=1
#             q.append([dy,dx])
#
# arr=[[1,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,1,0,1,1]]
# used=[[0]*5 for _ in range(5)]
# li=[]
# for i in range(5):
#     for j in range(5):
#         cnt = 0
#         if arr[i][j] == 1 and used[i][j]!=1:
#             used[i][j]=1
#             bfs(i,j)
#             li.append(cnt)
# print(f'섬개수 {len(li)}')
# print(f'가장 큰 사이즈 {max(li)}')
# print(f'가장 작은 사이즈 {min(li)}')



def bfs(y,x,k_y,k_x):
    q=deque()
    q.append([y,x,0,0])
    cnt = 0
    while q:
        node=q.popleft()
        nowy,nowx,level,cnt=node[0],node[1], node[2],node[3]
        if nowy==k_y and nowx==k_x:
            return level

        diry=[-1,1,0,0]
        dirx=[0,0,1,-1]

        for i in range(4):
            dy=diry[i]+nowy
            dx=dirx[i]+nowx
            if dy<0 or dy>3 or dx<0 or dx>5:continue
            if used[dy][dx]==1:continue
            if arr[dy][dx]==1 and cnt<2:
                used[dy][dx]==1
                q.append([dy,dx,level+1,cnt+1])
            elif arr[dy][dx]==0:
                used[dy][dx]==1
                q.append([dy,dx,level+1,cnt])


from collections import deque
arr=[[0,0,1,1,1,1],[0,0,1,0,0,1],[0,0,1,0,1,1],[0,0,1,0,1,0]]
used=[[0]*6 for _ in range(4)]
used[0][0]=1
a=bfs(0,0,3,5)
print(a)

















































