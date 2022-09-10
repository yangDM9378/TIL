n=int(input())
arr=['x','o']
path=['']*n
def abc(level):
    if level==n:
        for i in range(level):
            print(path[i],end='')
        print()
        return

    for i in range(len(arr)):
        path[level]=arr[i]
        abc(level+1)
        path[level]=0
abc(0)
