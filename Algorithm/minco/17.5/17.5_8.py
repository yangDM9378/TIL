map_arr=[[3,55,42],[-5,-9,-10]]
pix=[list(map(int, input().split())) for _ in range(2)]

def search_arr(a):
    for i in range(2):
        for j in range(3):
            if map_arr[i][j]==a:
                return 'Y'
    return 'N'
for a in range(2):
    for b in range(2):
        print(search_arr(pix[a][b]), end=' ')
    print()
