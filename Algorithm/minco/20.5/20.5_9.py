arr=[[3,5,4,2,5],[3,3,3,2,1],[3,2,6,7,8],[9,1,1,3,2]]
a,b=map(int, input().split())

def sum_arr(y,x):
    k=0
    for diry in range(a):
        for dirx in range(b):
            dy=y+diry
            dx=x+dirx
            if dy<0 or dy>3 or dx<0 or dx>4:
                continue
            k+=arr[dy][dx]
    return k

temp=0
for y in range(4):
    for x in range(5):
        rat=sum_arr(y,x)
        if rat>temp:
            temp=rat
            Maxy=y
            Maxx=x
print(f'({Maxy},{Maxx})')
