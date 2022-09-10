def eque():
    for i in range(n):
        if arr[minidx][i]==arr[j][i]:continue
        elif ord(arr[minidx][i])>ord(arr[j][i]):
            return j
        else:
            return minidx

n=int(input())

arr=[input() for _ in range(n)]

for i in range(n-1):
    minidx=i
    for j in range(i+1,n):
        if len(arr[minidx])>len(arr[j]):
            minidx=j
        elif len(arr[minidx])==len(arr[j]):
            minidx=eque()
    arr[i],arr[minidx]=arr[minidx],arr[i]
for l in range(n):
    print(arr[l])
