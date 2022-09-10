apt= [
    [15, 18, 17],
    [4, 6, 9],
    [10, 1, 3],
    [7, 8, 9],
    [15, 2, 6]
]
arr=list(map(int,input().split()))

def inPattern(i):
    for j in range(len(arr)):
        if apt[i][j]!=arr[j]:
            return 0
    return 1

for i in range(5):
    k=inPattern(i)
    if k==1:
        print(f'{5-i}층')