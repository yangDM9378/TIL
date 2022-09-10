arr=[3,5,4,2]
bit_arr=list(map(int, input().split()))
k=0
for i in range(4):
    if bit_arr[i]==1:
        k+=arr[i]
print(k)