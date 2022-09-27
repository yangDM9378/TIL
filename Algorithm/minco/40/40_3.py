k=list(map(int, input().split()))
dp=[-999]*100
arr=[0]*100
for i in range(len(k)):
    arr[i]=k[i]
dp[0]=0
dp[1]=0
dp[2]=arr[0]+arr[2]
dp[3]=arr[0]+arr[3]
for i in range(2,24):
    dp[i]=max(dp[i],dp[i-2]+arr[i])
    dp[i]=max(dp[i],dp[i-3]+arr[i])
    if i%2==0:
        dp[i]=max(dp[i],dp[i//2]+arr[i])
print(max(dp[12:]))

