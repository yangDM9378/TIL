arr=[[0,0,1,0,0],[0,0,1,1,1]]
arr1=[[3,5,4,1,1],[3,5,2,5,6]]

a=int(input())
def kkk(a,arr,arr1):
    for i in range(2):
        for j in range(5):
            if arr[i][j]==1 and arr1[i][j]==a:
                return f'{a} 존재'
    return f'{a} 없음'

print(kkk(a,arr,arr1))