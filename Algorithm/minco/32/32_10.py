n=int(input())

arr=[list(map(int, input().split())) for _ in range(n)]
z=[list(map(int, input().split())) for _ in range(n)]
li=[]
for i in range(n):
    for j in range(n):
        if z[i][j]==1:
            li.append(arr[i][j])

li=sorted(li, key=lambda x: (li.count(x),-x), reverse=True)
print(*li)