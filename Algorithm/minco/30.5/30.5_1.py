a=int(input())
k=(a//90)%4
arr=[12,9,3,6]
z=[0]*4
li=[1,3,0,2]
for _ in range(k):
    for i in range(4):
        z[i]=arr[li[i]]
    arr=z[:]
print(*z)