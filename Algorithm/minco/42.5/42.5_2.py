import copy
def boom(y,x,arr):
    cnt=0
    diry=[-1,1,0,0,0]
    dirx=[0,0,0,1,-1]
    for i in range(5):
        dy=diry[i]+y
        dx=dirx[i]+x
        if 0<=dy<4 and 0<=dx<4:
            if arr[dy][dx]!='_':
                cnt+=1
                arr[dy][dx]='_'
    return cnt, arr

def dfs(level,cnt):
    global arr
    global Max
    global result_path
    if level==N:
        if Max<cnt:
            Max=cnt
            result_path=copy.deepcopy(path)
        return

    for y in range(4):
        for x in range(4):
            if arr[y][x] != '_':
                path[level]=arr[y][x]
                arr_copy = copy.deepcopy(arr)
                result, arr= boom(y, x, arr)
                dfs(level+1,cnt+result)
                arr=arr_copy

arr=[list(input()) for _ in range(4)]
N=int(input())
result=0
path=[0]*3
Max=0
result_path=[]
dfs(0,0)
result_path.sort()
print(*result_path)