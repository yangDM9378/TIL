import copy

def result(arr):
    li = []
    gop_arr=1
    for i in range(N):
        print(arr)
        ssum = 0
        for j in range(N):
            ssum+=arr[j][i]
        li.append(ssum)
    for k in range(len(li)):
        gop_arr*=li[k]
    return gop_arr


def dfs(now):
    global Max_gop
    if now==N:
        ret=result(arr)
        Max_gop=max(Max_gop,ret)
        return
    for j in range(N):
        for i in range(N):
            arr[now][(i+j+1)%N]=path[now][i]
        dfs(now+1)

N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
path=copy.deepcopy(arr)
Max_gop=0
dfs(0)
print(f'{Max_gop}점')