

def adc(a_y,a_x,c):
    f_a_y=a_y+diry[i]
    f_a_x=a_x+dirx[i]
    if f_a_y<0 or f_a_y>3 or f_a_x<0 or f_a_x>2:
        return a_y, a_x
    if arr[f_a_y][f_a_x] == '_':
        arr[a_y][a_x]='_'
        arr[f_a_y][f_a_x] =c
        return f_a_y, f_a_x
    return a_y, a_x

arr=[list(input()) for _ in range(4)]
diry=[0,1,0,-1,0]
dirx=[1,0,-1,0,1]
a_y=0
a_x=1
d_y=1
d_x=2
c_y=2
c_x=0
for i in range(5):
    a_y,a_x=adc(a_y,a_x,'A')
    d_y,d_x=adc(d_y,d_x,'D')
    c_y,c_x=adc(c_y,c_x,'C')

for i in range(4):
    for j in range(3):
        print(arr[i][j], end='')
    print()
