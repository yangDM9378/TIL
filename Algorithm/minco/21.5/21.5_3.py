arr=list(input())
a=list(map(str, input().split()))
z_arr=[0]*len(arr)
for i in range(len(arr)):
    if arr[i] ==a[0] or arr[i]==a[1]:
        if (i-1)<0:
            z_arr[i+1] = '#'
        elif (i+1)>=len(arr):
            z_arr[i-1]='#'

        if (i-1)<0 or (i+1)>=len(arr):
            continue
        z_arr[i-1]='#'
        z_arr[i+1]='#'

for i in range(len(z_arr)):
    if z_arr[i]==0:
        z_arr[i]=arr[i]
    print(z_arr[i], end='')