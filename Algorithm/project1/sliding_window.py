# 이중  for 문
arr=[4,7,1,8,9,3,5,8,6,6,9]
# temp=0
# for i in range(len(arr)):
#     k=0
#     for j in range(5):
#         if (i+j)<len(arr):
#             k+=arr[i+j]
#
#     if temp<k:
#         temp=k
# print(temp)


# # 일중 for 문
# k=0
# for i in range(5):
#     k+=arr[i]
# Max_k=0
# for j in range(6):
#     k=k-arr[j]+arr[5+j]
#     if Max_k<k:
#         Max_k=k
# print(Max_k)

# # 가장 작은 영역 구하기
# ## 비효율적인 방법
# def minArray(nums, k):
#     result = sum(nums[0:k])
#     for i in range(1, len(nums)-(k-1)):
#         r = sum(nums[i:i+k])
#         if r < result:
#             result = r
#     return result
# ## 슬라이딩 윈도우
# def minSlidingWindow(nums, k):
#     min_sum = 9999
#     window_sum = 0
#     start = 0
#     for end in range(len(nums)):
#         window_sum += nums[end]
#         if end >= k - 1:
#             # 0~k-1 까지 더한 값이 최소값보다 작다면, 최소값을 갱신
#             if window_sum <= min_sum:
#                 min_sum = window_sum
#             # 윈도우에 포함된 맨 앞자리 수를 제거
#             window_sum -= nums[start]
#             # 윈도우 시작 인덱스를 하나 증가
#             start += 1
#     return min_sum
