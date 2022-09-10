a,b=map(int, input().split())
arr=[[0,0,1,0,1,1],[1,0,0,1,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0]]
used=[0]*6
sum=0
li_sum=[]

def dfs(now,b):
    global sum
    global li_sum
    if now==b:
        li_sum.append(sum)
    for i in range(6):
        if arr[now][i]!=0 and used[i]==0:
            used[i]=1
            sum+=arr[now][i]
            dfs(i,b)
            sum-=arr[now][i]
            used[i]=0
used[a-1]=1
dfs(a-1,b-1)
if len(li_sum)==0:
    print(0)
else:
    print(min(li_sum))