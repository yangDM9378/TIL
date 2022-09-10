def abc(a,b):

    print(a, end=' ')
    if a==b:
        return
    abc(a+1,b)
    print(a,end=' ')



a,b =map(int, input().split())
abc(a,b)