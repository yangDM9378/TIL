def findboss(member):
    global arr
    if arr[ord(member)]==0:
        return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(a,b):
    global arr
    aboss=findboss(a)
    bboss=findboss(b)
    if aboss==bboss:return 1
    arr[ord(bboss)]=aboss

t=int(input())
lst=[list(map(int,input().split())) for _ in range(t)]
li=[]
arr=[0]*200

for i in range(t):
    for j in range(t):
        if i<j:continue
        if lst[i][j]==1:
            li.append([chr(i+65),chr(j+65)])

cnt=0
for k in li:
    ret=union(k[0],k[1])
    if ret==1:
        cnt=1
        break

if cnt:print('cycle 발견')
else: print('미발견')