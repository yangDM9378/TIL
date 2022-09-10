arr=list(map(int, input().split()))

def max_num(a):
    for k in range(a,len(arr)):
        if pivot<arr[k]:
            return k
def min_num(b):
    for k in range(b,0,-1):
        if pivot>arr[k]:
            return k

pivot=arr[0]
a=1
b=len(arr)-1
while 1:
    if b<a:break
    temp=0
    a=max_num(a)
    b=min_num(b)
    arr[a],arr[b]=arr[b],arr[a]

arr[a],arr[b]=arr[b],arr[a]
arr[b],arr[0]=arr[0],arr[b]
for i in arr:
    print(i, end=' ')