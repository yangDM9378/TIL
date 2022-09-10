n=int(input())
path=[' ']*4
def abc(level):
    if level==4:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(n):
        path[level]=i+1
        abc(level+1)

abc(0)