a=list(map(int, input().split()))
for i in range(len(a)-1):
    a[i+1]=a[i]+a[i+1]

for i in a:
    print(i, end=' ')