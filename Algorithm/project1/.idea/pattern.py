# arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
# pattern=[3,5,8,4]
# flag=0
#
# def patternin(index):
#     for i in range(4):
#         if arr[index+i]!=pattern[i]:
#             return 0
#         return 1
#
# for j in range(11):
#     a=patternin(j)
#     if a==1:
#         flag=1
#         break
#
# if flag:
#     print('패턴')
# else:
#     print('패턴x')

board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"]
]

ptn = [list(input()) for _ in range(2)]
cnt=0
def f_pn(da,db):
    for i in range(2):
        for j in range(2):
            if board[da+i][db+j]!=ptn[i][j]:
                return 0
        return 1

for a in range(3):
    for b in range(2):
        if f_pn(a,b) ==1:
            cnt+=1
        print(cnt)
