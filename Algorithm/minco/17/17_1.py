arr=['M','T','K','C']

def isExist(arr,a):
    for i in range(len(arr)):
        if arr[i]==a:
            return  '발견'
    return '미발견'

a=input()
print(isExist(arr,a))