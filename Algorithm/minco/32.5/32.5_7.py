arr=[list(map(int,input().split())) for _ in range(4)]

def a(y,x,ly,lx):
    global li
    ssum = 0
    for dy in range(y,ly+1):
        for dx in range(x,lx+1):
            if arr[dy][dx] == 0:
                return li
            else:
                ssum+=arr[dy][dx]
    li.append(ssum)
    return li


li=[]
for y in range(4):
    for x in range(8):
        if arr[y][x]!=0:
            for ly in range(y, 4):
                for lx in range(x, 8):
                    if arr[y][x] != 0:
                        k=a (y,x,ly,lx)
print(max(k))
