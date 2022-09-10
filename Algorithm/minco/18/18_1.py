map_li=[
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]
z_li=[0]*65535
for i in range(3):
    for j in range(4):
        z_li[map_li[i][j]]+=1

temp=0
li=[]
for i in range(len(z_li)):
    if temp<z_li[i]:
        temp=z_li[i]
        li.append(i)
print(max(li))