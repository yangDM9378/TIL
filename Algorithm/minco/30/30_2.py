arr=[
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0]
]
cnt=0
used=[0]*6

def dfs(now):

    global cnt
    print(now, cnt)
    for i in range(6):
        if used[i]==1:continue
        if arr[now][i]!=0:
            cnt+=arr[now][i]
            used[i]=1

            dfs(i)


n=int(input())
used[n]=1
dfs(n)