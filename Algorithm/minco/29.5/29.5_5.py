arr=[list(map(int,input().split())) for _ in range(4)]

def abc(arr):
    for i in range(4):
        for j in range(5):
            if arr[i][j] == 1:
                return i,j

a,b=abc(arr)
print(f'({a},{b})')


for i in range(4):
    for j in range(5):
        if arr[i][j]==1:
            a,b=i,j
print(f'({a},{b})')