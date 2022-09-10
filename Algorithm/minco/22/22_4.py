cnt=1
def abc(level):
    global cnt
    if level==5:
        if cnt<0:
            cnt=cnt-1
            cnt='B'+str(-cnt)
        return
    n=input()
    if n=='up':
        cnt+=1
    else:
        cnt-=1
    abc(level+1)
abc(0)
print(cnt)