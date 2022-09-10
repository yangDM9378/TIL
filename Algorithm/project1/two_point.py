# n,target=map(int,input().split())
# arr=list(map(int,input().split()))
#
# cnt,sum=0,0
# high,low=0,0
# while(1):
#     if sum>target:        # 합이 타겟보다 크면.. (범위를 줄여야 하니까)
#         sum-=arr[low]       # sum에서 뺴고
#         low+=1              # low 의 index를 1증가
#     elif high==n: break
#     else:
#         sum+=arr[high]      # 합이 타겟보다 작거나 같다면
#         high+=1             # sum에 더하고 high의 인덱스를 1증가
#     if sum==target:
#         cnt+=1
# print(cnt)
#
# # 투 포인터 활용 기초. 시간문제를 어느정도 해결을 했으나, 비효율적임
# ## 투포인터 단순 풀이
# def simple_two_pointer(nums):
#     count = 0
#     start, end = 0, 0
#     while start <= end <= N:
#         r = sum(nums[start:end])
#         if r == M:
#             count += 1
#             end += 1
#         elif r < M:
#             end += 1
#         else:
#             start += 1
#     print(count)
#
# # 슬라이딩 윈도우에서 배열의 합을 효율적으로 계산하는 방법을 적용
# ## 투포인터
# def two_pointer(nums):
#     count = 0
#     start, end = 0, 0
#     window_sum = nums[start]
#     while start < N:
#         if window_sum == M:
#             count += 1
#             window_sum -= nums[start]
#             start += 1
#         elif window_sum < M:
#             end += 1
#             if end >= N:
#                 break
#             window_sum += nums[end]
#         else:
#             window_sum -= nums[start]
#             start += 1
#         print(f'start = {start} / end = {end}')