arr=[['A','7','9','T','K','Q'],['M','I','N','C','O','D']]
a,b =map(str, input().split())

def isExist(wo):
    for i in range(2):
        for j in range(6):
            if arr[i][j] == wo:
                return f'{wo} : 존재'

    return f'{wo} : 없음'

print(isExist(a))
print(isExist(b))