n=int(input())
arr=['A','B','C']
path=['']*n
cnt=0
def abc(level):
    global cnt
    if (level > 2 and path[level-1] == path[level-2]) and (path[level-3] == path[level-2]) :return
    if level==n:
        cnt += 1
        return

    for i in range(3):
        path[level]=arr[i]
        abc(level+1)

abc(0)
print(cnt)