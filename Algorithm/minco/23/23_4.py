arr=['B','T','S','K','R']
n=int(input())
path=['']*n
used=[0]*len(arr)
cnt=0
def abc(level):
    global cnt
    if level==n:
        if 'S' in path:
            cnt+=1
        return
    for i in range(len(arr)):
        if used[i] == 1: continue
        path[level]=arr[i]
        used[i] =1
        abc(level+1)
        used[i] = 0
        path[level]=0
abc(0)
print(cnt)