from collections import deque
def bfs(N,now):
    global arr
    q=deque()
    q.append([N,now])
    while q:
        print(q)
        node=q.popleft()
        cnt,now=node[0],node[1]

        if cnt==M:
            arr[cnt]=now
            break

        if arr[cnt]>now and 0<=cnt<=1000000:
            arr[cnt]=now
            q.append([N+1,now+1])
            q.append([N-1,now+1])
            q.append([N*2,now+1])
            q.append([N-10,now+1])


T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    arr=[21e8]*1000001
    bfs(N,0)
    print(arr[0:10])
