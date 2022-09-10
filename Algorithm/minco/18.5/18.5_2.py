arr=list(map(int, input().split()))
a=[0]*500
for i in range(len(arr)):
    a[arr[i]]+=1

def re(a):
    for j in range(len(a)):
        if a[j]>=2:
            return '도플갱어 발견'
    return '미발견'

print(re(a))

