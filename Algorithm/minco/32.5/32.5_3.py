def a(y,x):
    diry = [0, 1, -1, 0, 0]
    dirx = [0, 0, 0, 1, -1]
    for i in range(5):
        dy=y+diry[i]
        dx=x+dirx[i]
        if 0<=dx<=5 and 0<=dy<=2:
            if arr[dy][dx]!='#':
                arr[dy][dx]='#'
            else:
                arr[dy][dx]=arr_1[dy][dx]
    return arr


arr=[['A','B','C','E','F','G'],['H','I','J','K','L','M'],['N','O','P','Q','R','S']]
arr_1=[['A','B','C','E','F','G'],['H','I','J','K','L','M'],['N','O','P','Q','R','S']]
n=list(input())
for k in n:
    for y in range(3):
        for x in range(6):
            if arr[y][x]==k:
                arr=a(y,x)
for i in range(3):
    for j in range(6):
        print(arr[i][j], end='')
    print()