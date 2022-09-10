# 그래프-코드표현
# 1.인접행렬-열결되어 있는 곳에 1로 변환
#    A B C D E F
# arr=[[0,1,1,0,0,0],#A
#     [0,0,0,1,1,0],#B
#     [0,0,0,0,0,1],#C
#     [0,0,0,0,0,0],#D
#     [0,0,0,0,0,0],#E
#     [0,0,0,0,0,0]]#F
# # 2.인접리스트
# brr=[
#     [1,2], #A
#     [3,4], #B
#     [5], #C
#     [],
#     [],
#     []
# ]
# 3.일차원리스트(이진트리에 한해서)
## 부모인덱스 1 왼쪽자식=부모*2  오른쪽자식=부모*2+1


## 인접행렬 연습
# name=['A','B','C','E','D']
# arr=[ [0,1,1,0,0],
#       [0,0,0,1,0],
#       [0,1,0,0,0],
#       [0,0,0,0,1], # E
#       [0,1,0,0,0]  # D
# ]
# sum=0
# Max=0
# Maxindex=0
# for j in range(5):
#       sum=0
#       for i in range(5):
#            if arr[i][j]==1:
#                  sum+=1
#       if sum>Max:
#             Max=sum
#             Maxindex=j
# print(name[Maxindex])
### 문자 하나를 입력 받아 주셍.
### 입력 받은 문자의 형제 출력
### A입력시 형제 없음
### B입력시 C 출력
### E입력시 D 출력
### F입력시 형제 없음 이 출력되면 됩니다.
# name=['A','B','C','D','E','F']
# arr=[[0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
# # 1.부모찾기 출력하기
# # 2.형제찾아 출력하기
# ch=input()
# idx=ord(ch)-65
# answer=[]
#
# for i in range(6):
#     if ar[i][idx]==1:
#         answer.append(i)
#
# if len(answer)==0:
#     print("형제없음")
# else:
#     result=[]
#     for x in answer:
#         for i in range(6):
#             if ar[x][i]==1:
#                 result.append(i)
#     result.remove(idx)
#     if len(result)==0:
#         print("형제없음")
#     else:
#         for x in result:
#             print(chr(x+65))
