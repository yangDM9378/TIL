# arr=[[4,7,1,8],[5,5,9,2],[5,9,5,9],[1,2,9,7]]
# diry=[0,0,-1,1]
# dirx=[1,-1,0,0]
#
# def pat(y,x):
#     sum=0
#     for i in range(4):
#         dy=diry[i]+y
#         dx=dirx[i]+x
#
#         if dx<0 or dx>3 or dy<0 or dy>3:
#             continue
#         sum+=arr[dy][dx]
#     return sum
#
# temp=0
#
# for y in range(4):
#     for x in range(4):
#         rat=pat(y,x)
#         if temp<rat:
#             temp=rat
#             Maxy=y
#             Maxx=x
# print(temp)
# print(Maxy, Maxx)
#

#
# arr=[[4,7,1,8],[3,5,9,2],[5,9,5,9],[1,2,9,7]]
#

#
# '''
# 반시계방향으로 45도 회전된 대각선 합
# '''
# result = [0]*(2*N-1)
# for y in range(N):
#     for x in range(N):
#         result[(N-1-y)+x] += arr_2d[y][x]
# print(result)
#




# arr=[[4,7,1,8],[3,5,9,2],[5,9,5,9],[1,2,9,7]]
#
# sum_hi=0
# sum_lo=0
# for y in range(4):
#     for x in range(4):
#         if y<3-x:
#             sum_hi+=arr[y][x]
#         elif y>3-x:
#             sum_lo+=arr[y][x]
#
# print(sum_hi, sum_lo)
