def dfs(now):
    global Max
    global Min
    if now==5:
        k=(path[0]*path[1])-(path[2]*path[3])+path[4]
        Min=min(Min,k)
        Max=max(Max,k)
        return

    for i in range(len(arr)):
        if used[i]==1:continue
        path.append(arr[i])
        used[i]=1
        dfs(now+1)
        used[i]=0
        path.pop()

arr=list(map(int, input().split()))
used=[0]*5
Max=-21e8
Min=21e8
path=[]
dfs(0)
print(Max)
print(Min)
