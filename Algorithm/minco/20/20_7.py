def abc(n):
    if n==0:
        return
    abc(n//2)
    print(n,end =' ')

n=int(input())
abc(n)