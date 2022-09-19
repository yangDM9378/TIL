
# 트리모양 DFS
name=['A','B','C','D','E','F']
arr=[[0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

li=[]
def dfs(now):
    global li
    li.append(name[now])
    for i in range(6):
        if arr[now][i]==1:
            dfs(i)
dfs(0)
print(li)

#연습
# name=['K','F','C','D','M','G','A']
# arr=[[0,1,1,1,0,0,0],
#     [0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#      ]
# li=[]
# def dfs(now):
#     global li
#     li.append(name[now])
#     for i in range(7):
#         if arr[now][i]==1:
#             dfs(i)
# dfs(0)
# print(li)

# ## 트리모양 아닌 DFS
# name=['A','B','C','D']
# li=[]
# arr=[[0,1,0,0],[0,0,1,1],[1,0,0,1],[0,0,0,0]]
# used=[0]*4
# def dfs(now):
#     global li
#     li.append(name[now])
#     for i in range(4):
#         if used[i] == 1:continue
#         if arr[now][i]==1:
#             used[i]=1
#             dfs(i)
# now=2
# used[now]=1
# dfs(now)
# print(li)
# ## 경로탐색-경로갯수
# name=['A','B','C','D']
# li=[]
# arr=[[0,1,1,0],[0,0,1,1],[0,1,0,1],[0,0,0,0]]
# used=[0]*4
# cnt=0
# def dfs(now):
#     global cnt
#     if now==3:
#         cnt+=1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
# now=1
# used[now]=1
# dfs(now)
# print(cnt)
# ## 경로탐색 문제
# ### 출발점 입력받기
# ### 출발점 알파벳 부터 E가 써있는 곳까지 갈수 있는 방법 몇가지 있는지 출력
# word=input()
# name=['A','B','C','D','E']
# now=name.index(word)
# arr=[[0,1,0,0,0],[0,0,1,1,1],[1,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]
# used=[0]*5
# cnt=0
# li=[]
# li.append(name[now])
# def dfs(now):
#     global cnt
#     if now==4:
#         cnt+=1
#         print(li)
#     for i in range(5):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             li.append(name[i])
#             dfs(i)
#             li.pop()
#             used[i]=0
# used[now]=1
# dfs(now)
# print(cnt)

# ## 최소비용 문제
# word=input()
# name=['A','B','C','D','E']
# now=name.index(word)
# arr=[[0,4,0,0,0],[0,0,1,2,9],[5,0,0,7,0],[0,0,0,0,1],[0,0,0,0,0]]
# used=[0]*5
# sum=0
# li_sum=[]
# def dfs(now):
#     global sum
#     if now==4:
#         li_sum.append(sum)
#     for i in range(5):
#         if arr[now][i]!=0 and used[i]==0:
#             used[i]=1
#             sum+=arr[now][i]
#             dfs(i)
#             sum-=arr[now][i]
#             used[i]=0
# used[now]=1
# dfs(now)
# print(min(li_sum))

## 합이 최대
# arr=[
#     [2,5,7],
#     [8,4,-8],
#     [-7,1,4],
#     [5,1,9]
# ]
# Max=int(-21e8)
#
# def dfs(level, sum):
#     global Max
#     if level==4:
#         if sum>Max:
#             Max=sum
#         return
#
#     for i in range(3):
#         dfs(level+1,sum+arr[level][i])
#
# dfs(0,0) # level sum
# print(Max)

# 0은벽/아래 3방향으로 이동
# 배열범위 벗어나지 못함
# 최대합 구하기
#
# arr=[[3,2,4,1],[0,1,0,5],[2,0,3,0],[5,4,0,2],[2,-5,0,3]]
# Max=-11111111111
# def dfs(now, level, sum):
#     global Max
#     if level == 5:
#         if sum > Max:
#             Max = sum
#         return
#     for i  in range(3):
#         direct = [-1, 0, 1]
#         dy=level
#         dx=now+direct[i]
#         if dx<0 or dx>3: continue
#         if arr[dy][dx]==0:continue
#         dfs(dx,level+1, sum+arr[dy][dx])
#
# for i in range(4):
#     dfs(i,0,0)
# print(Max)

# DFS 미로찾기
# 0길 and 1벽
# 도착할수 있냐
# arr=[[0,0,0,0],[1,0,1,0],[1,0,1,0],[0,0,0,0]]
# visit=[[0]*4 for _ in range(4)]
# flag=0 #도착시 1로 바꿀
#
# def dfs(y,x):
#
#     global flag
#     if y==3 and x==3:
#         flag=1
#         return
#
#     diry=[-1,1,0,0]
#     dirx=[0,0,-1,1]
#
#     for i in range(4):
#         dy=y+diry[i]
#         dx=x+dirx[i]
#         if dy<0 or dy>3 or dx<0 or dx>3:continue
#         if visit[dy][dx]==1:continue
#         if arr[dy][dx]==1: continue
#         visit[dy][dx]=1
#         dfs(dy,dx)
# visit[0][0]=1
# dfs(0,0)
# if flag==1:
#     print('갈수있어~!')
# else:
#     print('도착 x')

# # 미로찾기 (DFS) _ 최단거리 출력
# # 최소 몇번 이동을 해야할까요???
# arr=[[0,0,0,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1],
#      [0,0,0,0,0]]
# diry = [1, -1, 0, 0]
# dirx = [0, 0, -1, 1]
# used=[[0]*5 for _ in range(4)]
# cnt=0
# min_in=99999999999999
# def dfs(y,x):
#     global cnt
#     global min_in
#     if y==1 and x==3:
#         if min_in >= cnt:
#             min_in=cnt
#         return
#
#     for i in range(4):
#         dy=y+diry[i]
#         dx=x+dirx[i]
#         if dy<0 or dy>3 or dx<0 or dx>4:continue
#         if used[dy][dx]==1:continue
#         if arr[dy][dx]==1: continue
#         cnt+=1
#         used[dy][dx]=1
#         dfs(dy,dx)
#         cnt-=1
#         used[dy][dx]=0
#
# used[0][0]=1
# dfs(0,0)
# print(min_in)


# # 미로 경로(여러개 경로갯수)
# def dfs(i,j,N):
#     global answer
#     if maze[i][j]==3:
#         answer+=1
#         return
#     else:
#         visited[i][j]=1
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj=i+di, j+dj
#             if maze[ni][nj]!=1 and visited[ni][nj]==0:
#                 dfs(ni, nj, N)
#         visited[i][j] = 0
#         return
#
# T= int(input())
# for tc in range(1, T+1):
#     N=int(input())
#     maze=[list(map(int, input())) for _ in range(N)]
#     sti=-1
#     stj=-1
#     # 출발점 찾기
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j]==2:
#                 sti, stj=i,j
#                 break
#         if sti != -1:
#             break
#     answer = 0#가능한 모든경로수
#     visited=[[0]*N for _ in range(N)]
#     dfs(sti,stj,N)


# # 미로 경로(여러 경로까지 최단거리)
# def dfs(i,j,s,N):
#     global minV
#     if maze[i][j]==3:
#         #출발치 포함 경로수여서 +1
#         if minV > s+1:
#             minV = s+1
#         return
#     else:
#         visited[i][j]=1
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj=i+di, j+dj
#             if maze[ni][nj]!=1 and visited[ni][nj]==0:
#                 dfs(ni, nj,s+1 N)
#         visited[i][j] = 0
#         return
#
# T= int(input())
# for tc in range(1, T+1):
#     N=int(input())
#     maze=[list(map(int, input())) for _ in range(N)]
#     sti=-1
#     stj=-1
#     # 출발점 찾기
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j]==2:
#                 sti, stj=i,j
#                 break
#         if sti != -1:
#             break
#     answer = 0#가능한 모든경로수
#     minV=N*N
#     visited=[[0]*N for _ in range(N)]
#     dfs(sti,stj,0,N)
#     # 도착 못하는 경우 초기값 나옴
#     if minV==N*N:
#         minV=-1
#     print(minV)