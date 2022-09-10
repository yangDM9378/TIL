arr=list(input())
path=[' ']*3
used=[0]*len(arr)
def abc(level):
    if level==3:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(4):
        if used[i]==1:continue
        path[level]=arr[i]
        used[i]=1
        abc(level+1)
        used[i]=0
        path[level]=0
abc(0)