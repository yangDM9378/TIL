T=int(input())
diry=[0,0,1]
dirx=[1,-1,0]


def shift(y,x):
    a = y
    b = x
    while True:
    for i in range(3):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>99 or dx<0 or dx>99:
            continue
        if arr[dy][dx]==2:
            return a,b
        if dy==99:
            return 0

for t in range(T):
    while True:
        arr[y][x]
        if y==99:
            break
        if arr[y][x]==2:
            print(y,x)

