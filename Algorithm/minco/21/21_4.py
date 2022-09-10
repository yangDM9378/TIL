lev=int(input())
k=lev
def level(lev):
    print(k-lev, end='')
    if lev==0:
        return

    for i in range(2):
        level(lev-1)

level(lev)