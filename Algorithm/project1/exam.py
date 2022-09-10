# 자료구조, 자료를 관리하는 방식 queue stack
#
# # stack 자료구조의 특성

# stack 사용법
# s=[0,1,2,3]
# s.append(2)
# s.append(7)
# s.append(3)
# s.pop()
# s.append(9)
# s.pop()
# s.append(7)
# s.append(2)
# s.pop()

# 선택정렬
# O(n^2)
# 구현쉽다 느리다
# arr=[4,7,1,3,5,2]
# for y in range(len(arr)-1):
#     for x in range(y+1,len(arr)):
#         if arr[y]>arr[x]:
#             temp=arr[y]
#             arr[y]=arr[x]
#             arr[x]=temp


## n입력 -> 5
## n*n배열을 입력
# 5
# 2 4 7 4 2
# 2 9 5 3 1
# 4 9 6 5 3
# 3 7 9 2 3
# 1 1 2 3 4
## 1. 배열 전체 평균 구하기
## 2. 각좌표값이 배열평균과 차이는 값들의 합 출력
# n=int(input())
# arr=[list(map(int, input().split())) for _ in range(5)]
# print(arr)
# sum = 0
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         sum+=arr[i][j]
#         cnt+=1
# print(int(sum/cnt))
# k=int(sum/cnt)

# 패턴찾기
# n*m배열을 입력
# 5 4 배열
# 1 1 1 1
# 1 0 1 1
# 1 0 1 1
# 1 1 0 1
# 1 0 1 1
# 1 1
# 1 0
# n,m=map(int, input().split())
# arr=[list(map(int, input().split())) for _ in range(5)]
# pat=[[1,1],[1,0]]
#
# def pattern(y,x):
#     flag=0
#     for dy in range(2):
#         for dx in range(2):
#             if arr[y+dy][x+dx]!=pat[dy][dx]:
#                 return 0
#     return 1
# rat=0
# for y in range(n-1):
#     for x in range(m-1):
#         rat+=pattern(y,x)
#
# print(rat)

# n,m 입력
# 2차원 배열 입력 후
# 위아래 좌우 기준 좌표보다 크면 산봉우리
# 4 5
# 2 4 2 1 5
# 1 2 1 4 3
# 2 2 2 4 2
# 1 7 3 2 3
#
# n,m=map(int, input().split())
# arr=[list(map(int, input().split())) for _ in range(n)]
#
# def tks(y,x):
#     diry=[1,-1,0,0]
#     dirx=[0,0,-1,1]
#     for i in range(4):
#         dy=y+diry[i]
#         dx=x+dirx[i]
#         if dy<0 or dy>3 or dx<0 or dx>3: continue
#         if arr[y][x]<=arr[dy][dx]:
#             return 0
#     return 1
# cnt=0
# for y in range(n):
#     for x in range(m):
#         cnt+=tks(y,x)
# print(cnt)
