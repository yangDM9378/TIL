arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
result=[0]*8
arr1.sort()
arr2.sort()
arr1_i=0
arr2_i=0
i=0
while i<=6:
    if arr1[arr1_i] >= arr2[arr2_i]:
        result[i]=arr2[arr2_i]
        arr2_i+=1
        i+=1
        if arr2_i==4:
            for k in range(arr1_i,4):
                result[i]=arr1[k]
                i+=1
    else:
        result[i]=arr1[arr1_i]
        arr1_i+=1
        i+=1
        if arr1_i==4:
            for k in range(arr2_i,4):
                result[i]=arr2[k]
                i+=1

for z in result:
    print(z, end=' ')

