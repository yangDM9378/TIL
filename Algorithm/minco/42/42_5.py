def dfs(now,ssum):
    global cnt
    if now==n:
        if ssum==10:
            cnt+=1
        return
    for i in range(9):
        dfs(now+1,ssum+arr[i])

arr=[1,2,3,4,5,6,7,8,9]
n=int(input())
cnt=0
dfs(0,0)
print(cnt)