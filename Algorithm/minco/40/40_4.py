arr=[list(map(int, input().split())) for _ in range(7)]
dp=[[-999]*3 for _ in range(7)]
dp[0][0]=1
for i in range(6):
    for j in range(3):
        if arr[i][j]!=0:
            if j==0:
                if arr[i+1][j+1]!=0:
                    dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+arr[i+1][j+1])
                if arr[i+1][j]!=0:
                    dp[i+1][j]=max(dp[i+1][j],dp[i][j]+arr[i+1][j])
            elif j==2:
                if arr[i+1][j-1]!=0:
                    dp[i+1][j-1]=max(dp[i+1][j-1],dp[i][j]+arr[i+1][j-1])
                if arr[i+1][j]!=0:
                    dp[i+1][j]=max(dp[i+1][j],dp[i][j]+arr[i+1][j])
            else:
                if arr[i+1][j-1]!=0:
                    dp[i+1][j-1]=max(dp[i+1][j-1],dp[i][j]+arr[i+1][j-1])
                if arr[i+1][j]!=0:
                    dp[i+1][j]=max(dp[i+1][j],dp[i][j]+arr[i+1][j])
                if arr[i+1][j+1]!=0:
                    dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+arr[i+1][j+1])



print(max(dp[-1]))