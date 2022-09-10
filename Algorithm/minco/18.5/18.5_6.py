win=[[3,5,1],[4,2,6]]
people=map(int, input().split())

def su(a):
    for i in range(2):
        for j in range(3):
            if win[i][j]==a:
                return f'{a}번 합격'
    return f'{a}번 불합격'

for a in people:
    print(su(a))