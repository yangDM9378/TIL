li=[[0]*3 for _ in range(6)]
i=65
for y in range(2,-1,-1):
    for x in range(5,-1,-1):
        li[x][y]=chr(i)
        i+=1
a,b=map(int, input().split())
print(li[a][b])