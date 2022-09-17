import copy
def dfs(arr):
    global path, Max, result
    if arr==['_']*N:
        if Max<sum(path):
            Max=sum(path)
            result=copy.deepcopy(path)
        return

    arr_copy=copy.deepcopy(arr)
    for i in range(N):
        if arr[i]!='_':
            path.append(arr[i])
            if (i-1)<0:
                arr[i]='_'
                arr[i+1]='_'
            elif (i+1)>N-1:
                arr[i]='_'
                arr[i-1]='_'
            else:
                arr[i]='_'
                arr[i+1]='_'
                arr[i-1]='_'
            dfs(arr)
            arr=arr_copy
            path.pop()

N=int(input())
arr=list(map(int,input().split()))
path=[]
Max=0
result=[]
dfs(arr)
for i in range(len(result)):
    print(result[i], end='')
    if len(result)-1==i:
        print('=', end='')
    else:
        print('+', end='')
print(sum(result))