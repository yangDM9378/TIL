
def rk(s,l):
    Max=-1
    while 1:
        m=(s+l)//2
        if arr[m][0]=='0':
            l=m-1
        elif arr[m][0]=='#':
            Max=m
            s=m+1
        if s>l:
            break
    return Max

def tp(s,l,y):
    Maxx=-1
    while 1:
        m=(s+l)//2
        if arr[y][m]=='0':
            l=m-1
        elif arr[y][m]=='#':
            Maxx=m
            s=m+1
        if s>l:
            break
    return Maxx+1

T = int(input())
arr=[]
for _ in range(T):
    arr.append(input())
y=rk(0,T-1)
x=tp(0,T-1,y)
print(y,x-1)
