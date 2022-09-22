# # 미로찾기
# arr=[[0,1,1,9],[4,2,2,3],[1,3,4,1],[3,7,8,0]]
# dp=[[0]*4 for _ in range(4)]
# # 시작지점부터 1행과 1열 누적합으로 채워주기
# for i in range(1,4):
#     dp[0][i]=dp[0][i-1]+arr[0][i]
#     dp[i][0]=dp[i-1][0]+arr[i][0]
#
# for i in range(1,4):
#     for j in range(1,4):
#         dp[i][j]=min(dp[i-1][j],dp[i][j-1])+arr[i][j]
# print(dp)

# # knapsack
# n, k = map(int, input().split())
# knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 배열
#
# item = [[0, 0]]
# for i in range(1, n + 1):  # 아이템 입력
#     item.append(list(map(int, input().split())))
#
# for i in range(1, n + 1):  # 아이템 개수만큼 반복
#     for j in range(1, k + 1):  # 최대무게까지 반복
#
#         weight = item[i][0]
#         value = item[i][1]
#
#         if j < weight:  # 가방에 넣을 수 없으면
#             knapsack[i][j] = knapsack[i - 1][j]  # 위에 값 그대로 가져오기
#         else: # 가방에 넣을 수 있으면
#             knapsack[i][j] = max(knapsack[i - 1][j],value + knapsack[i][j - weight])
#             # 위에 값 vs
#             # 현재 아이템 가치 + 그전 단계에서 구한 남은무게의 가치
#
# print(knapsack[n][k])