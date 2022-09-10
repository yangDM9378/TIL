board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"],
    ["A", "B", "C", "T"]
]
btn=[
    ["A","B"],
    ["T","T"],
    ["C","T"]
]

def a(i,j):
    for x in range(3):
        for y in range(2):
            if board[x+i][y+j]!=btn[x][y]:
                return 0
    return 1

cnt=0
for i in range(2):
    for j in range(3):
        if a(i,j)==1:
            cnt+=1

if cnt!=0:
    print('발견')
else:
    print('미발견')