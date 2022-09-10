arr=[[3,5,9],[4,2,1],[5,1,5]]

def isExist(arr,a):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == a:
                return f'{a}:존재'
    return f'{a}:미발견'

a,b,c=map(int, input().split())
print(isExist(arr,a))
print(isExist(arr,b))
print(isExist(arr,c))