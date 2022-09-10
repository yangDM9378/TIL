n=int(input())
arr=list(map(int, input().split()))
target=int(input())

def binary_search(s,e,value):
    while (1):
        m=(s+e)//2
        if arr[m]>value:
            e=m-1
        elif arr[m]<value:
            s=m+1
        else:
            return 1
        if s>e:
            return 0

arr.sort()
ret=binary_search(0,n-1,target)

if ret:
    print('존재')
else:
    print('없음')