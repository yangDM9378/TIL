arr=[1,2,3,3,5,1,0,1,3]
n=int(input())
result=0
for i in range(n):
    result+=arr[i]
min_result=result
for j in range(len(arr)-n):
    result=result-arr[j]+arr[n+j]
    if min_result>result:
        min_result=result
print(min_result)