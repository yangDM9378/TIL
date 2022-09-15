def dfs(now,gop):
    global path, result, min_gop
    if now==M:
        if min_gop>gop:
            min_gop=gop
            result=path[:]
        return

    for i in range(N):
        if used[i] == 1:continue
        used[i]=1
        path.append(arr[i])
        dfs(now+1, gop*arr[i])
        used[i]=0
        path.pop()




N,M=map(int, input().split())
arr=list(map(int,input().split()))
path=[]
result=''
used=[0]*N
min_gop=99999
dfs(0,1)
result=sorted(result)
print(*result)