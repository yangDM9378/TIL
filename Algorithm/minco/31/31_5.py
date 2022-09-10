n=int(input())
arr=list(map(str,input().split()))
result='HITSMUSIC'

cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==result:
            cnt+=1
print(cnt)