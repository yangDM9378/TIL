# LCS(longest common string)
def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    arr = [[0] * (len2 + 1) for i in range(len1 + 1)]
    Max=0
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                Max=max(Max,arr[i][j])
            else:
                arr[i][j] = 0
    return Max
s1 = "BABJYP"
s2 = "ABCBJY"
print("Length of LCS is ", lcs(s1, s2))


# LCS(longest common subquence)
def lcs(s1,s2):
    arr=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    Max=0
    for i in range(1,len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
            Max=max(Max,arr[i][j])
    print(arr)
    return Max

s1='BABJYP'
s2='ABPABY'
print(lcs(s1,s2))

