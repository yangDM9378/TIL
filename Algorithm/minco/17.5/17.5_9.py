arr=list(map(int, input().split()))
mask=[1,0,1,0,1,0]
temp=9999
for i in range(6):
    if mask[i]==1:
        if arr[i]<temp:
            temp=arr[i]
            k=i
print(f'arr[{k}]={temp}')