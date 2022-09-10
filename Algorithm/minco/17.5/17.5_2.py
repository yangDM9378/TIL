arr=[3,7,4,1,2,6]
li=[list(map(int, input().split())) for _ in range(2)]


def isExist(arr, li):
    for i in range(2):
        for j in range(2):
            if li[i][j] in arr:
                li[i][j]='OK'
            else:
                li[i][j]='NO'
    return li
ex_li=isExist(arr,li)
for i in range(2):
    for j in range(2):
        print(ex_li[i][j],end=' ')
    print()