# LIS(longest increasing subquence)
# 최장공통부분수열
arr=[10,20,10,30,20,50]
result=[1]*len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            result[i]=max(result[i],result[j]+1)
print(result)