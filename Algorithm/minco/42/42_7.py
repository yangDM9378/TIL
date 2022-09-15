def dfs(now,ssum):
    global Max_sum
    if now==len(gbag)-n:
        if ssum%10==0:
            if Max_sum<ssum:
                Max_sum=ssum
        return
    for i in range(len(gbag)):
        if used[i]==1:continue
        used[i]=1
        dfs(now+1,ssum+arr[ord(gbag[i])-97])
        used[i]=0



gbag=list(input())
used=[0]*len(gbag)
n=int(input())
Max_sum=0
arr=[15,20,44,22,55,16,45]
dfs(0,0)
print(Max_sum)