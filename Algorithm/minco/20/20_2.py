arr=list(map(int, input().split()))

def movement(a):

    if a==len(arr)-1:
        print(arr[a],end=' ')
        return
    print(arr[a],end=' ')
    movement(a+1)
    print(arr[a],end=' ')

movement(0)