def a(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i-1] and arr[i-1] == arr[i-2]:
            arr.pop(i)
            arr.pop(i-1)
            arr.pop(i-2)
            a(arr)
        if i==len(arr)-1:
            return arr




T=int(input())
arr=list(map(int,input().split()))

k=a(arr)

print(*sorted(k))