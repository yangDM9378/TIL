T=int(input())
arr=[list(map(str, input().split())) for _ in range(T)]
for i in range(len(arr)):
    arr[i][1]= int(arr[i][1])
print(arr[0][0])
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j][1]>=arr[j-1][1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
    k=arr[:i+1]
    if len(k)>3:
        k=k[:3]
    for z in range(len(k)):
        print(k[z][0],end=' ')
    print()
