T=int(input())
arr=[list(map(str,input().split())) for _ in range(T)]
for k in range(len(arr)):
    arr[k][0]=int(arr[k][0])

for j in range(1,len(arr)):
    for i in range(j,0,-1):
        if arr[i][0]<arr[i-1][0]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
        elif arr[i][0]==arr[i-1][0]:
            if ord(arr[i][1])<ord(arr[i-1][1]):
                arr[i], arr[i-1]=arr[i-1],arr[i]
for i in range(len(arr)):
    for j in range(2):
        print(arr[i][j], end=' ')
    print()