a=list(map(int, input().split()))
for i in range(4, 8):
    k=a[0:i]
    for j in k:
        print(j,end=' ')
    print('')

