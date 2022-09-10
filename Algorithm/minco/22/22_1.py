arr=['A','B','C']
path=[' ']*len(arr)
def abc(lev):
    if lev==2:
        for i in range(lev):
            print(path[i],end='')
        print()
        return

    for j in range(3):
        path[lev]=arr[j]
        abc(lev+1)
        path[lev]=0

abc(0)

