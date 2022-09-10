n=int(input())
arr=list(map(int, input().split()))

result=0
for i in range(4):
    result+=arr[i]
min_arr=result
for j in range(n-4):
    result=result-arr[j]+arr[4+j]
    if min_arr > result:
        min_arr=result
print(min_arr)
