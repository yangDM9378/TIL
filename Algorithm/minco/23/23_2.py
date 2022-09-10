word=list(input())
path=['']*4
cnt=0
def abc(level):
    global cnt
    if level==4:
        cnt += 1
        return
    for i in range(4):
        if level>0 and (path[level-1]=='B' and word[i]=='T') or (path[level-1]=='T' and word[i]=='B'):continue
        path[level]=word[i]

        abc(level+1)
        path[level]=0

abc(0)
print(cnt)