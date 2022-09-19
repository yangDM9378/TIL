# arr=[1,2,3,4]
# n=int(input())
# cnt=0
# li=[]
# def dfs(now):
#     global cnt
#     global li
#     if now==n:
#         return
#     if cnt==10:
#         print(li)
#         return
#     for i in range(len(arr)):
#         cnt+=arr[i]
#         li.append(arr[i])
#         dfs(now+1)
#         cnt-=arr[i]
#         li.pop()
#
# dfs(0)

# def dfs(now,start):
#     global li
#     if now==3:
#         print(*li)
#         return
#
#     for i in range(start,4):
#         if used[i]==0:
#             li.append(arr[i])
#             used[i]=1
#             dfs(now+1,i+1)
#             li.pop()
#             used[i]=0
#
#
# used=[0]*4
# arr=['M','B','T','I']
# li=[]
# dfs(0,0)


# 두 라인에서 숫자를 1개씩 번갈아 가며 선택을
# 하고자 합니다.
# 첫번째 라인에서 숫자를 1개 택한 후 *1을 하고
# 두번째 라인에서 숫자를 1개 택한 후 *2를 하고
# 첫번쨰 라인에서 숫자를 1개 택한 후 *3을 하고..
# 두번째 라인에서 숫자를 1개 택한 수 *4를 하는등
# 가중치가 1씩 증가되는 값으로 뽑은 숫자에 곱해 줍니다.
#
# 가중치를 곱한 후 모두 더했을때
# 합이 0에 가장 가까운 수를 구하고자 합니다.
# 이때 총 합은 몇일까요?
# (각 라인의 숫자는 1번씩만 사용하여 모든 숫자를 한번씩 뽑습니다.)
# line1=[3,7,1,-3,-6,1]
# line2=[7,-4,1,-5,3,2]
# used1=[0]*6
# used2=[0]*6
#
# Min=21e8
# answer=21e8
#
# def dfs(level,sum):
#     global Min,answer,used1,used2
#     if level==12:
#         # 0에 가장 가까운 sum
#         if Min>abs(sum):
#             Min=abs(sum)
#             answer=sum
#         return
#
#     if level%2==0:
#         for i in range(6):
#             if used1[i]==1: continue
#             used1[i]=1
#             dfs(level+1,sum+(line1[i]*(level+1)))
#             used1[i]=0
#     else:
#         for i in range(6):
#             if used2[i]==1: continue
#             used2[i]=1
#             dfs(level+1,sum+(line2[i]*(level+1)))
#             used2[i]=0
#
# dfs(0,0) #level,sum
# print(answer)
#
# # 설계시..
# # 그림그려보기
# # dfs함수 (매개변수) // 리턴조건 //
# # dfs 몇번호출 // used 사용여부 // level br




# # 서바이벌 게임
# # a ~ g 를 두팀으로 나누어서
# # 게임을 하고자 합니다.
# # 두 팀으로 나누었을때
# # 두 팀의 전투력 차이가 최소가 되었을때
# # 최소 전투력 차이는 몇일까요?
# # 모든 선수는 경기에 참가를 하며
# # 1인팀도 가능 합니다.
# power=[50,40,99,5,25,6,37]
# check=[0]*7
# Min=21e8
#
# def dfs(start,level,sum):
#     global Min,power
#     against=0
#     for i in range(7):
#         if check[i]==0:
#             against+=power[i]
#     gap=abs(sum-against)
#     Min=min(Min,gap)
#
#     if level==6:
#         return
#     for i in range(start,7):
#         check[i]=1
#         dfs(i+1,level+1,sum+power[i])
#         check[i]=0
# dfs(0,0,0) # start,level,sum
# print(Min)




# # [7 3 5 4]
# # 각각의 숫자에
# # 2를 곱하거나 또는
# # 3으로 나누거나 또는
# # 5를 더해서 숫자를 바꾼 후
# #
# # 바뀐 4개의 숫자들의 곱을 구한 후
# # 그 곱의 Max값을 출력해 주세요.
# #
# # (추가설명)
# # 7 3 5 4 가 있다면
# # 7에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# # 3에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# # 5에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# # 4에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# #
# # 바뀐 숫자들을 모두 곱했을때 MAX 값 출력하기
# n=4
# arr=[7,3,5,4]
# Max=-21e8
#
# def dfs(level):
#
#     global  Max
#     if level==4:
#         gop=1
#         for i in range(4):
#             gop*=arr[i]
#             Max=max(Max,gop)
#         return
#
#     backup=arr[level]
#
#     arr[level]*=2
#     dfs(level+1)
#     arr[level]=backup     # 원상복구
#
#     arr[level]/=3
#     dfs(level+1)
#     arr[level]=backup    # 원상복구 arr[level]*=3 (X)
#
#     arr[level]+=5
#     dfs(level+1)
#     arr[level]=backup   # 원상복구
#
# dfs(0)
# print(Max)

# 땅파기 문제
# 땅을 개척작업을 통해
# 가치를 올리고자 합니다.
# (위아래좌우그리고 자기자신의 가치가 *7한수 %10한 값으로 바뀜)
#
# 총 3곳을 개발할 예정..
# 중복가능( 한번 개발한 했던곳을 또 개발 가능)
# 개발후 3*3배열의 땅의가치가 MAx가 되었을때
# 그 MAx값을 출력해 주시면 됩니다.

import copy
arr=[[4,2,1],[5,3,9],[7,8,1]]

Max=-21e8

def digging(y,x):
    directy=[0,-1,1,0,0]
    directx=[0,0,0,-1,1]
    for i in range(5):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx]=(arr[dy][dx]*7)%10

# def getsum():
#     sum=0
#     for i in range(3):
#         for j in range(3):
#             sum+=arr[i][j]
#     return sum
#
# def dfs(level):
#     global Max,arr
#     backup=copy.deepcopy(arr)
#
#     if level==3:
#         ret=getsum()
#         Max=max(Max,ret)
#         return
#
#     for i in range(3):
#         for j in range(3):
#             digging(i,j)
#             dfs(level+1)
#             arr=copy.deepcopy(backup)
#
# dfs(0)
# print(Max)