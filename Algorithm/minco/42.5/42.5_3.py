import copy
def dfs(level, result):
    global cnt
    if level==N-1:

        if result == 100:
            cnt += 1
        return
    if result>100:
        return

    dfs(level+1, (result-arr[level+1])*(result+arr[level+1]))
    dfs(level+1, max(arr[level+1],result))
    dfs(level+1, (result**2)-(arr[level+1]**2))
    dfs(level+1, (result+arr[level+1])**2)

N=int(input())
arr=list(map(int,input().split()))
used=[0]*3
cnt=0
dfs(0, arr[0])
print(cnt)