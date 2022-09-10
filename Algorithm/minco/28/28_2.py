n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

boss=[]
for i in range(n):
    if arr[i][0]==1:
       boss.append(i)

under=[]
for i in range(n):
    if arr[0][i]==1:
        under.append(i)
print('boss:',end='')
print(*boss)
print('under:', end='')
print(*under)