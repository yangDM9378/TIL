arr=[['G','K','Y'],['P','A','C']]
a=list(map(str, input().split()))


def isExist():
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] in a:
                cnt+=1
    return cnt

if isExist()==2:
    print('대발견')
elif isExist() == 1:
    print('중발견')
else:
    print('미발견')