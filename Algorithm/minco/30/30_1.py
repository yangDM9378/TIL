arr=[[0,0,1,1,0,1],[0,0,0,1,1,1],[0,0,0,0,1,1],[0,0,0,0,0,0],[1,0,0,0,0,1],[0,0,0,0,0,0]]
used=[0]*6
now=int(input())
li=[]
def dfs(now):
    global li
    li.append(now)
    for i in range(6):
        if used[i]==1:continue
        if arr[now][i]==1:
            used[i]=1
            dfs(i)


used[now]=1
dfs(now)
print(*li)