import copy
def score(arr):
    cnt=0
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            cnt-=50
        elif abs(ord(arr[i])-ord(arr[i-1]))<=5:
            cnt+=3
        elif abs(ord(arr[i])-ord(arr[i-1]))>=20:
            cnt+=10
    return cnt


def dfs(level,a):
    global arr, Max_score, dfs_cnt
    if level==N:
        result=score(arr)
        dfs_cnt+=1
        if Max_score<result:
            Max_score=result
        return
    for i in range(a,len(arr)-1):
        for j in range(i+1,len(arr)):
            if [i,j] in used:continue
            used.append([i,j])
            arr_copy = copy.deepcopy(arr)
            arr[i], arr[j]=arr[j], arr[i]
            dfs(level+1,i)
            used.pop()
            arr = arr_copy


arr=list(input())
N=int(input())
Max_score=0
used=[]
dfs_cnt=0
dfs(0,0)
print(Max_score)
