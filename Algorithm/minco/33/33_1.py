def findboss(member):
    global arr
    if arr[ord(member)]==0:
        return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(a,b):
    global arr
    aboss,bboss=findboss(a),findboss(b)
    if aboss==bboss: return 1
    arr[ord(bboss)]=aboss
    return 0
k=int(input())
arr=[0]*200
cnt=0
for i in range(k):
    a,b = map(str, input().split())
    ret=union(a,b)
    cnt+=ret
if cnt==1:
    print('발견')
else:
    print('미발견')

