n=int(input())
arr=['시작',3,1,2,1,3,2,1,2,1,'도착']

def jump(a):
    if arr[a]=='도착':
        return

    if a==0:
        print(arr[a], end=' ')
        a+=n
    else:
        print(arr[a], end=' ')
        a+=arr[a]
    jump(a)
    print(arr[a], end=' ')
    if a==n:
        a-=n
        print(arr[a], end=' ')

jump(0)