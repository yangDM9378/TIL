def abc(a):
    if a==len(arr):
        print()
        return
    print(arr[a],end='')
    abc(a+1)
    print(arr[a], end='')



arr=list(input())
abc(0)