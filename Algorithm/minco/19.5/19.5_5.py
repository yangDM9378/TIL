arr=[['A','B','G','K'],['T','T','A','B'],['A','C','C','D']]
a=[list(input()) for _ in range(2)]


def pattern(y,x):
    for i in range(2):
        for j in range(2):
            if arr[i+y][j+x]!=a[i][j]:
                return 0
    return 1

flag=0
for y in range(2):
    for x in range(3):
        k=pattern(y,x)
        flag+=k

if flag>=1:
    print(f'발견({flag}개)')
else:
    print('미발견')