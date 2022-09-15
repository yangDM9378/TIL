def findboss(member):
    global lst
    if lst[ord(member)]==0:
        return member
    ret=findboss(lst[ord(member)])
    return ret

def union(a,b):
    global lst
    aboss, bboss=findboss(a), findboss(b)
    if aboss==bboss:
        return
    lst[ord(bboss)]=aboss

N=int(input())
arr=list(map(int, input().split()))
lst=[0]*200
for _ in range(int(input())):
    state, a, b=map(str, input().split())
    if state=='alliance':
        union(a,b)
        print(lst[65:65+N])

    else:
        pass

