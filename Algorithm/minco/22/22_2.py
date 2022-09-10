arr=[input() for _ in range(3)]
cnt=0
a=''
def abc(lev):
    global cnt
    global a
    if lev==3:
        if arr[lev-1] == arr[0]:
            cnt+=1
        return
    if arr[lev]==a:
        cnt+=1
    a=arr[lev]
    abc(lev+1)

abc(0)
if cnt==3:
    print('WOW')
elif cnt==2:
    print('GOOD')
else:
    print('BAD')