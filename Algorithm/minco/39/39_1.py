arr=list(map(int, input().split()))
arr.sort()
result=0
for i in range(len(arr)):
    result+=arr[i]*(len(arr)-i-1)
print(result)