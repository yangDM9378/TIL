a,b=map(int, input().split())

def abc(a,b):
    arr=['_','_','_','_','_']
    if b==0:
        for i in range(5):
            print(arr[i], end='')
        return
    arr[a]=b
    for k in range(5):
        print(arr[k], end='')
    print()
    abc(a+1,b-1)
abc(a,b)