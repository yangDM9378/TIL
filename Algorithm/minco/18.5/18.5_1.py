arr=[['G','K','G'],list(map(str,input().split()))]
z_li=[0]*26

for i in range(2):
    for j in range(3):
        z_li[ord(arr[i][j])-65]+=1
flag=0
for k in range(len(z_li)):
    if z_li[k]>=3:
        flag=1

if flag!=1:
    print('없음')
else:
    print('있음')