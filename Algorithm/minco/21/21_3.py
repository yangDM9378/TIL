level=int(input())
branch=int(input())

def lev_bran(level, branch):
    if level==0:
        return

    for _ in range(branch):
        lev_bran(level-1,branch)

lev_bran(level, branch)
