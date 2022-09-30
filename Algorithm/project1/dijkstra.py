name='ABCDE'
inf=int(21e8)
arr=[
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0],
]
used=[0]*5
result=[0,3,inf,9,5]
used[0]=1 # 시작점 'A'라고 가정함


def select_ky():
    Min=int(21e8)
    Minindex=0
    for i in range(5):
        if(used[i]==0 and result[i]<Min):
            Min=result[i]
            Minindex=i
    return Minindex

def dijkstra():
    for _ in range(4):
        via=select_ky() # 경유지 선택
        used[via]=1
        for j in range(5): # 모든 정점에 대한 비용을 비교
            baro=result[j]  # 시->도
            ky=result[via]+arr[via][j] # 시->경->도
            if baro>ky:
                result[j]=ky
        print(result)
dijkstra()
print(*result)

#
# 개선된 다익스트라
# 5
# 7
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3
import heapq
name='ABCDE'
n=int(input())
m=int(input())
arr=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    arr[a].append((b,c))
start,ed=map(int,input().split())
inf=int(21e8)
result=[inf]*n
heap=[]

def dijkstra(start):
    heapq.heappush(heap,(0,start))   # 처음에는 시작점을 경유지로 놓기 (비용 경유지)
    result[start]=0                  # 그 다음 부터는 heapq에서 최소 비용을 다음 경유지로 선택

    while heap:
        sk,k=heapq.heappop(heap)    # sk=시작점에서 경유지 까지 비용  그리고  k= 경유지

        if result[k]<sk: continue   #  result 에서의 업데이트 되어있는 시작점에서->경유지 값 vs
                                    # 큐에서 방금 뽑은 시작점에서->경유지 값 이랑 비교

        for i in arr[k]:   # 모든 정점에 대해서 (경유지에서 도착할 수 있는 정점을 비교)
            cost=sk+i[1]   # cost = 시->경유지 비용 + 경유지에서 도착점까지 최소비용
            if cost<result[i[0]]:
                result[i[0]]=cost
                heapq.heappush(heap,(cost,i[0]))

dijkstra(start)
print(*result)
