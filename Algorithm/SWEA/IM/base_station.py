# 1
# 9
# XXXXXXXXX
# XXXHXXXXX
# XXHAHXXHX
# XXHHXXXXX
# XXXXXXXXX
# XXBHHXXXX
# XXHXXHAHX
# XXAHXXHXX
# XXHXHXXXX

def a(y,x):
    diry=[-1,1,0,0]
    dirx=[0,0,1,-1]
    for i in range(4):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1:
            continue
        if arr[dy][dx]=='H':
            arr[dy][dx]='X'
    return arr

def b(y,x):
    diry=[-2,-1,2,1,0,0,0,0]
    dirx=[0,0,0,0,1,2,-1,-2]
    for i in range(8):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1:
            continue
        if arr[dy][dx] == 'H':
            arr[dy][dx] = 'X'
    return arr


def c(y,x):
    diry=[-3,-2,-1,3,2,1,0,0,0,0,0,0]
    dirx=[0,0,0,0,0,0,1,2,3,-1,-2,-3]
    for i in range(12):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1:
            continue
        if arr[dy][dx] == 'H':
            arr[dy][dx] = 'X'
    return arr



T=int(input())
for t in range(T):
    N=int(input())
    arr=[list(input()) for _ in range(9)]
    for y in range(N):
        for x in range(N):
            if arr[y][x]=='A':
                arr=a(y,x)
            elif arr[y][x]=='B':
                arr=b(y,x)
            elif arr[y][x]=='C':
                arr=c(y,x)
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='H':
                cnt+=1
    print(f'#{t+1} {cnt}')