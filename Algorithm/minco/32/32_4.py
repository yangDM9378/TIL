arr=[list(input()) for _ in range(5)]
a,b=map(int,input().split())
arr[a].sort()
arr[b].sort()
for i in range(len(arr)):
    print(arr[i][0], end=' ')