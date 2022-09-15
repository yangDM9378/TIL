def dfs(ssum):
    global cnt
    global min_cnt

    if ssum==money:
        min_cnt=min(min_cnt,cnt)
        return
    if ssum>money:
        return

    for i in range(3):
        ssum+=arr[i]
        cnt+=1
        dfs(ssum)
        ssum-=arr[i]
        cnt-=1

money=int(input())
arr=[10,40,60]
cnt=0
min_cnt=21e8
dfs(0)
print(min_cnt)