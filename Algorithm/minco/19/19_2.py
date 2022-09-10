arr= [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]
a=[-1,1,-1,1]
b=[-1,1,1,-1]

def sum_arr(y,x):
    k=0
    for i in range(4):
        dy=y+a[i]
        dx=x+b[i]
        if dx<0 or dx>4 or dy<0 or dy>4:
            continue
        k+=arr[dy][dx]
    return k

temp=int(-21e8)
for y in range(5):
    for x in range(5):
        ret=sum_arr(y,x)
        if ret>temp:
            temp=ret
            Maxy=y
            Maxx=x
print(Maxy,Maxx)