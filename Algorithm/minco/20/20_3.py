def abc(n):
    global cnt
    if cnt==3:
        print(n, end=' ')
        return
    cnt+=1
    abc(n+2)
    print(n, end=' ')

cnt=0
n = int(input())
abc(n)