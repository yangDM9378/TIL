a=input()

def abc(a):
    print(a, end=' ')
    if a==1:
        return
    abc(a-1)
    print(a, end=' ')


abc(len(a))