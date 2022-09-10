n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
name=[0,1,2,3,4,5,6]

def dfs(now):
    print(now,end=' ')
    for i in range(n):
        if arr[now][i]==1:

            dfs(i)


dfs(0)
