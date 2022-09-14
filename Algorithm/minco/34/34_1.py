arr=[4,4,5,7,8,10,20,22,23,24]

def binary_search(s,l,n):
    while 1:
        m=(s+l)//2
        if s>l:
            return 0

        if arr[m]==n:
            return 1

        if arr[m] > n:
            s=s
            l=m-1
        else:
            s=m+1
            l=l

n=int(input())
s=0
l=len(arr)-1
ret=binary_search(s,l,n)
if ret: print('O')
else: print('X')