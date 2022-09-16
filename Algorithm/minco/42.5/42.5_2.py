import copy
def boom(y,x):
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

def dfs(level):
    global result
    global arr
    global Max
    global result_path
    if level==N:
        if Max<result:
            Max=result
            result_path=path
        return
    for y in range(4):
        for x in range(4):
            if arr[y][x] != '_':
                arr_copy = copy.deepcopy(arr)
                path[level]=arr[y][x]
                cnt, kkk = boom(y, x)
                result+=cnt
                dfs(level+1)
                arr=arr_copy
                result-=cnt



arr=[list(input()) for _ in range(4)]
N=int(input())
result=0
path=[0]*3
Max=0
result_path=[]
dfs(0)
print(result_path)