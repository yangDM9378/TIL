img=[list(map(int, input().split())) for _ in range(4)]
diry=[0,1,0,1,0,1]
dirx=[0,0,1,1,2,2]
def rectSum(y,x):
    a=0
    for i in range(len(diry)):
        dy=y+diry[i]
        dx=x+dirx[i]
        a+=img[dy][dx]
    return a

temp=-111111111
for i in range(3):
    for j in range(2):
        if temp<rectSum(i,j):
            temp=rectSum(i,j)
            Maxy=i
            Maxx=j

print(f'({Maxy},{Maxx})')