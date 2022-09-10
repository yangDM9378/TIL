arr=[[3,5,1],[3,8,1],[1,1,5]]
b=[list(map(int, input().split())) for _ in range(2)]

def sum_ma(y,x):
    sum_max=0
    for i in range(2):
        for j in range(2):
            sum_max+=arr[y+i][x+j]*b[i][j]
    return sum_max

temp=-11111111111111
for y in range(2):
    for x in range(2):
        ret=sum_ma(y,x)
        if temp<ret:
            temp=ret
            maxy=y
            maxx=x

print(f'({maxy},{maxx})')