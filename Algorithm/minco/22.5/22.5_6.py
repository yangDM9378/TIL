arr=[input() for _ in range(4)]
arr=sorted(arr, key=len)
for i in range(4):
    print(arr[i])