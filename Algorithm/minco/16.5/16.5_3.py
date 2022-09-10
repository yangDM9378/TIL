
arr=[[0]*3 for _ in range(2)]
a=list(map(int, input().split()))
for k in range(len(a)):
    arr[k//3][k%3]=a[k]

def max_li(li):
    temp=li[0][0]
    for i in range(2):
        for j in range(3):
            if li[i][j]>=temp:
                temp=li[i][j]
                li_i,li_j=i,j
    return f'({li_i},{li_j})'

def min_li(li):
    temp=li[0][0]
    for i in range(2):
        for j in range(3):
            if li[i][j]<=temp:
                temp=li[i][j]
                li_i, li_j = i, j
    return f'({li_i},{li_j})'


print(max_li(arr))
print(min_li(arr))