arr=[0]*200
arr[ord('B')] = 'A'
arr[ord('C')] = 'A'
arr[ord('D')] = 'E'
arr[ord('F')] = 'E'
arr[ord('J')] = 'I'
arr[ord('G')] = 'H'

def findboss(member):
    global arr
    if arr[ord(member)]==0:
        return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(a,b):
    global arr
    aboss, bboss=findboss(a),findboss(b)
    if aboss==bboss:
        return
    arr[ord(bboss)]=aboss

k=int(input())
for _ in range(k):
    a,b= map(str, input().split())
    union(a,b)

cnt=0
lst='ABCDEFGHIJ'
for i in lst:
    if arr[ord(i)]==0:
        cnt+=1
print(f'{cnt}개')