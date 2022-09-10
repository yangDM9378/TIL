arr=list(['_']*5 for _ in range(4))
diry=[0,0,-1,1,1,1,-1,-1]
dirx=[1,-1,0,0,1,-1,1,-1]

def booom(y,x):
    for i in range(8):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>3 or dx<0 or dx>4:
            continue
        arr[dy][dx]='#'
    return arr
for i in range(2):
    y, x = map(int, input().split())
    arr=booom(y,x)

for i in range(4):
    for j in range(5):
        print(arr[i][j], end=' ')
    print()