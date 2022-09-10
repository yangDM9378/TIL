T=int(input())

for _ in range(T):
    a=list(input())
    arr=[chr(65+i) for i in range(26)]
    sum=0
    for i in range(len(a)):
        k=(26**(3-i))*(ord(a[i])-65)
        sum+=k
    print(sum+1)