branch, level=map(int,input().split())
cnt=0
def lev_bran(branch,level):
    global cnt
    cnt+=1

    if level==0:
        return
    for _ in range(branch):
        lev_bran(branch,level-1)
    return cnt

print(lev_bran(branch,level))