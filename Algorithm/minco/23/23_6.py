arr=[int(i) for i in list(input())]
path=[0]*4
cnt=0
def abc(level):
    global cnt
    if level==4:
        cnt+=1
        return

    for i in range(len(arr)):
        path[level]=arr[i]
        if level > 0 and (abs(path[level] - path[level - 1]) > 3): continue
        abc(level+1)
        path[level]=0

abc(0)
print(cnt)