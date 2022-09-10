# bfs 사이클 없는 경우
# arr = [
#     [0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]
# def bfs(start_node):
#     queue = [start_node]
#     while queue:
#         node = queue.pop(0)
#         print(node, end=' ')
#         for i in range(len(arr[node])):
#             if arr[node][i]==1:
#                 queue.append(i)
#
# bfs(0)

# arr = [
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0]
# ]
# # bfs 사이클이 있는 경우
# def bfs(start_node):
#     queue = [start_node]
#     used = [0] * 4
#     used[start_node]=1
#     while queue:
#         node = queue.pop(0)
#         print(node, end=' ')
#         for i in range(len(arr[node])):
#             if arr[node][i] == 1:
#                 if used[i] == 0:
#                     used[i] = 1
#                     queue.append(i)
# bfs(0)

# 그래프 G와 탐색 시작점 v
# def BFS(G,v,n)
#     visited=[0]*(n+1)  #정점의 개수
#     queue=[]
#     queue.append(v)
#     visited[1]=1
#     while queue:
#         t=queue.pop(0)
#         visit(t)
#         for i in G[t]:
#             if not visited[i]
#                 queue.append(i)
#                 visited[i]=visited[t]+1

# 방향성 없는 그래프
# def bfs(v,N):
#     visited = [0]*(N+1)
#     q=[]
#     q.append(v)
#     visited[v]=1
#     while q:
#         v=q.pop(0)
#         print(v)
#         for w in adjlist[v]:
#             if visited[w]==0:
#                 q.append(w)
#                 visited[w]=visited[v]+1
# V,E=map(int, input().split())
# N=V+1   # 정점개수
# adjlist=[[] for _ in range(N)]
# for _ in range(E):
#     a,b=map(int, input().split())
#     # 양방향
#     adjlist[a].append(b)
#     adjlist[b].append(a)
# bfs(0,V) # 시작점, 종료지점

# 방향있는 그래프
# def bfs(v,N, t): # 시작, N 마지막, 찾는
#     visited = [0]*(N+1) # 인덱스 말고 노드번호로 하기위해
#     q=[]
#     q.append(v)
#     visited[v]=1
#     while q:
#         v=q.pop(0)
#         if v==t:
#             return 1 #목표발견(목표 좌표 찾기)
#             rutnrn visited[99] #목표 지점까지 거리
#         return 0 #목표없음
#         for w in adjlist[v]:
#             if visited[w]==0:
#                 q.append(w)
#                 visited[w]=visited[v]+1
# V,E=map(int, input().split())
# N=V+1   # 정점개수
# adjlist=[[] for _ in range(N)]
# for _ in range(E):
#     a,b=map(int, input().split())
#     # 양방향
#     adjlist[a].append(b)
#     adjlist[b].append(a)
# bfs(0,V) # 시작점, 종료지점

# # 미로(1개)
# def bfs(i,j,N):
#     visited=[[0]*N for _ in range(N)]
#     q=[]
#     q.append((i,j))
#     visited[i][j]=1
#     while q:
#         i,j = q.pop(0)
#         if maze[i][j]# 도착지 3번인가
#             return 1
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni,nj=i+di,j+dj
#             if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited==0:
#                 q.append((ni,nj))
#                 visited[ni][nj]=visited[i][j]+1
#     return 0
#
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
#     print(f'#{tc} {bfs(sti, stj, N)}')
