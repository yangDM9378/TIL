arrA=list(map(int, input().split()))
arrB=list(map(int, input().split()))

for i in range(len(arrA)):
    re=arrA[i]+arrB[(len(arrA)-1)-i]
    print(re, end=' ')