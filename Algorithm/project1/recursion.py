#
# def abc(level):
#     if level==2:
#         return
#
#     abc(level+1)
#     debug=1
#
# abc(0)


# def abc(a):
#     print(a, end=' ')
#     if a==5:
#         return
#     abc(a+1)
#     print(a, end=' ')
# abc(1)
#

#
#
#
def abc(a):
    if a==0:
        return
    print(a, end=' ')
    abc(a-1)
    print(a, end=' ')
abc(6)


# def abc(a):
#     print(a, end=' ')
#     if a==9:
#         print(a, end=' ')
#         return
#
#     abc(a+2)
#     print(a, end=' ')
#
# abc(1)
#
# def abc(lev):
#     if lev==2::
#         return
#
#     for i in range(2):
#         print('#', end=' ')
#         abc(lev+1)
#
# abc(0)

# def abc(level):
#     # print('#', end='')
#     if level==2:
#         # print('#', end='')
#         return
#     # print('#', end='')
#     for i in range(2):
#         # print('#', end='')
#         abc(level+1)
#         # print('#', end='')
#     print('#', end='')
#
#
# abc(0)

# * 누적합 구하기 (재귀 들어가면서 누적합 출력하기)
# 전역변수로 놓고하기
# arr=[3,4,5,1,6,9]
# sum=3
# def abc(level):
#     global sum
#     if level==5:
#         print(sum)
#         return
#     print(sum)
#     sum+=arr[level+1]
#     abc(level+1)
# abc(0)
# 매개변수로 하기
# def abc(level,sum):
#     if level==5:
#         print(sum)
#         return
#     print(sum)
#     abc(level+1,sum+arr[level+1])
#
# abc(0,3) # level sum

# 전역변수와 매개변수 차이 들어갔다 나올때 차이가 발생
# 전역은 나올때 변수가 고정됨
# 매개변수는 나올때 변수가 그전 변수로 바뀜
# arr=[3,4,5,1,6,9]
# sum=0
# def abc(level):
#     global sum
#     if level==6:
#         return
#     sum+=arr[level]
#     abc(level+1)
#     print(sum)
#     sum-=arr[level]
#
# abc(0)

# def abc(level,sum):
#     if level ==5:
#         print(sum)
#         return
#
#     abc(level+1, sum+arr[level+1])
#     print(sum)
#
# abc(0,3)

# 누적합 연습
## 전역
# arr=[5,9,7,3,1,5,6,4]
# sum=arr[0]
# def abc(level):
#     global sum
#     if level==len(arr)-1:
#         print(sum)
#         return
#     print(sum)
#     sum+=arr[level+1]
#     abc(level+1)
#     sum -= arr[level+1]
#     print(sum)
#
# abc(0)

## 매개
# def abc(level,sum):
#     if level==len(arr)-1:
#         print(sum)
#         return
#     print(sum)
#     abc(level+1, sum+arr[level+1])
#     print(sum)
#
# abc(0,sum)

## 연습
# arr=[2,0,1,1,3,5,1]
# def abc(level):
#     if level>len(arr)-1:
#         return
#
#     abc(level+arr[level])
#     print(arr[level])
#
# abc(0)

# arr=[3,7,1,5]
# def abc(level,sum):
#     if level==3:
#         print(sum, end=' ')
#         return
#
#     for i in range(len(arr)):
#         abc(level+1, sum+arr[i])
#
# abc(0,0)

# arr=[4,-7,1,3]
# cnt=0
# def abc(level, sum):
#     global cnt
#     if level == 4:
#         if sum>10:
#             cnt+=1
#         return
#     for i in range(4):
#         abc(level+1,sum+arr[i])
#
# abc(0,0)
# print(cnt)
#
# n=int(input())
# coin=[100,70,10]
# li=[]
# def abc(lev, n):
#     global li
#     if n==0:
#         li.append(lev)
#         return
#     if n<0:
#         return
#     for i in range(3):
#         abc(lev+1,n-coin[i])
# abc(0,n)
# print(min(li))

## 재귀 경로 출력
# arr=['a','b','c']
# path=[' ']*5
# def abc(level):
#     if level==2:
#         for i in range(level):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
## 중복순열
# arr=['a','b','c']
# path=['']*5
#
#
# def abc(level):
#     if level==2:
#         for i in range(level):
#             print(path[i],end=' ')
#         print()
#         return
#
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
#
# abc(0)

# # 순열
# n=int(input())
# path=['']*n # 최대 레벨 까지 size 맞추면 오케이
# dice=[1,2,3,4,5,6]
# used=[0]*6  # br의 개수 만큼 만들기
# def abc(level):
#     if level==n:
#         for i in range(level):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(6):
#         #if used[i]==0:
#         if used[i] == 1: continue
#         path[level]=dice[i]
#         used[i] =1
#         abc(level+1)
#         used[i] = 0
#         path[level]=0
# abc(0)

## 순열 연습
# n=int(input())
# path=[' ']*n
# arr=['A','B','C','D']
# used=[0]*len(arr)
# def abc(level):
#     if level==n:
#         for i in range(n):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(len(arr)):
#         if used[i]==1:continue
#         path[level]=arr[i]
#         used[i]=1
#         abc(level+1)
#         used[i]=0
#         path[level]=0
# abc(0)

## 특정 브랜치 진입x
## 진입 x
# n=int(input())
# arr=['A','B','C','D']
# path=[' ']*len(arr)
# def abc(level):
#     if level == n:
#         for i in range(level):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(len(arr)):
#         if level==0 and arr[i]=='C':continue
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
# abc(0)
## 진입 후 리턴
# n=int(input())
# arr=['A','B','C','D']
# path=[' ']*len(arr)
# def abc(level):
#     if level==1 and path[level-1]=='C': return
#     if level == n:
#         for i in range(level):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(len(arr)):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
# abc(0)
## 진입 x
# n=int(input())
# arr=['A','B','C','D']
# path=[' ']*len(arr)
# def abc(level):
#     if level == n:
#         for i in range(level):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(len(arr)):
#         if arr[i]=='B': continue
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
# abc(0)
## 진입 후 리턴
# n=int(input())
# arr=['A','B','C','D']
# path=[' ']*len(arr)
# def abc(level):
#     if level>0 and path[level-1]=='B': return
#     if level == n:
#         for i in range(level):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(len(arr)):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
# abc(0)

## 연속으로 같은 값 출력 x
n=int(input())
arr=['A','B','C','D']
path=[' ']*len(arr)
def abc(level):
    if level>1 and path[level-1]==path[level-2]: return
    if level == n:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(len(arr)):
        if level>0 and path[level-1]==arr[i]:continue
        path[level]=arr[i]
        abc(level+1)
        path[level]=0
abc(0)