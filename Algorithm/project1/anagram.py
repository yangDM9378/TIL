# arr1 = input()
# arr2 = input()
# board1 = [0] * 26
# board2 = [0] * 26
# for i in (arr1):
#     board1[ord(i) - ord('a')] += 1
# for i in (arr2):
#     board2[ord(i) - ord('a')] += 1
#
# flag = 1
# for i in range(26):
#     if board1[i] != board2[i]:
#         flag = 0
#         break
# if flag:
#     print('anagram')
# else:
#     print('not anagram')
# # ===============================================
# vect1 = input()
# vect2 = input()
# if sorted(vect1) == sorted(vect2):
#     print('아나그램')
# else:
#     print('아나그램 아님')

# ================================================
# 두단어를 애너그램으로 만들기 위한 제거할 최소글자
# a='aabbc'
# b='eebbff'
#
# dat=[0]*26
# for i in a:
#     dat[ord(i)-ord('a')]+=1
#
# for i in b:
#     dat[ord(i)-ord('a')]+=1
#
# cnt=0
# for i in range(26):
#     if dat[i]!=0:
#         cnt+=abs(dat[i])
#
# print(cnt)
# ==================================================================
# 두 문자열 s1,s2를 입력받은 후 s2의 연속 부분 문자열 중 s1의 아나그램 개수를 출력해 주세요.
# 'abcab'
# 'aabbcbbaa'

s1=input()
s2=input()

cnt=0
if sorted(s1)==sorted(s2[0:len(s1)]):
    cnt+=1
for i in range(len(s2)-len(s1)):
    if sorted(s1)==sorted(s2[i:i+len(s1)]):
        cnt+=1
print(cnt)
