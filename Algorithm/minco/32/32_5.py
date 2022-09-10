n=int(input())
arr=[input() for _ in range(n)]

arr1=sorted(arr, key=lambda x: (len(x),x))
for k in range(n):
    print(arr1[k])