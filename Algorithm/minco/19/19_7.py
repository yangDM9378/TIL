vect=[[0]*3 for i in range(4)]

for _ in range(4):
    a,b=map(int, input().split())
    vect[a][b]=5

for i in range(4):
    for j in range(3):
        print(vect[i][j], end=' ')
    print()