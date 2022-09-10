T=int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
y = 5
x = 5
for _ in range(T):
    word=input()
    if word=='click':
        print(f'{y},{x}')
    else:
        if word=='up':
            y=y+dy[0]
            x=x+dy[0]
        elif word=='down':
            y=y+dy[1]
            x=x+dx[1]
        elif word=='lift':
            y=y+dy[2]
            x=x+dx[2]
        else:
            y=y+dy[3]
            x=x+dx[3]