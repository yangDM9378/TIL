N=input()
level=3
arr=['A','B','C','D']
path=[' ']*3
cnt=0
def abc(lev):
    global cnt


    if lev==3:
        cnt+=1
        if path[0] == N[0] and path[1] == N[1] and path[2] == N[2]:
            print(f'{cnt}번째')
        return

    for i in range(len(arr)):
        path[lev]=arr[i]
        abc(lev+1)
abc(0)