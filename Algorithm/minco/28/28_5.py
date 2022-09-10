n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
path=[0]*3
level=1
def bfs(now):
    global level
    if level == 3:
        for k in range(3):
            print(path[k], end=' ')
        print()
        return
    for i in range(n):
        if arr[now][i]==1:
            path[level]=i
            level+=1
            bfs(i)
            level-=1

bfs(0)