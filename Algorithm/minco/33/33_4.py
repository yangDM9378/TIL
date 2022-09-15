def findboss(member):
    global lst
    if lst[member]==0:
        return member
    ret=findboss(lst[member])
    return ret

def union(a,b):
    global lst
    aboss, bboss=findboss(a), findboss(b)
    if aboss==bboss:
        return
    lst[bboss]=aboss

N,K=map(int, input().split())
lst=[0]*(K+1)
arr=[list(map(str, input().split())) for _ in range(N)]
for i in arr:
    if ord(i[0])<65 and ord(i[1])<65:
        union(int(i[0]),int(i[1]))
        print(lst)
    else:
        pass

