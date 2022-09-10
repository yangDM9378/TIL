arr=[list(map(int, input().split())) for _ in range(5)]
diry=[1,-1,0,0,-1,-1,1,1]
dirx=[0,0,-1,1,-1,1,1,-1]

def re_arr(y,x):
    for i in range(8):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>4 or dx<0 or dx>3:
            continue
        if arr[dy][dx]==1:
            return 1
    return 0
flag=0
for y in range(5):
    for x in range(4):
        if arr[y][x]==1:
            flag+=re_arr(y,x)
if flag==0:
    print('안정된 상태')
else:
    print('불안정한 상태')