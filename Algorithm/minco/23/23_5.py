x=input()
arr=['E','W','A','B','C']
path=['']*4
used=[0]*len(arr)
def abc(level):
    if level==4:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(arr)):
        if used[i]==1:continue
        if arr[i]==x:continue
        path[level]=arr[i]
        used[i]=1
        abc(level+1)
        path[level]=0
        used[i]=0
abc(0)