lev=int(input())
arr=['B','G','T','K']
path=[' ']*lev
def abc(level):
    if level == lev:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(len(arr)):
        path[level]=arr[i]
        abc(level+1)

abc(0)