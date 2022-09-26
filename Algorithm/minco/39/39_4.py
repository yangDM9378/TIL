N=int(input())
arr=list(map(int, input().split()))
arr.sort()
k=100
cnt=0
for i in range(len(arr)):
    k=k-arr[i]
    if k>=0:
        cnt+=1
print(cnt)