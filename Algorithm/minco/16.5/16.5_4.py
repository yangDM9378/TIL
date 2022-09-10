index0, index1=map(int, input().split())
arr=[0]*6
arr[0]=index0
arr[1]=index1

for i in range(2,len(arr)):
    arr[i]=arr[i-2]*arr[i-1]
print(arr[-1])