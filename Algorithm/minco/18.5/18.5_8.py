dat=[0]*25

for i in range(3):
    arr=list(input())
    for j in range(len(arr)):
        dat[ord(arr[j])-65]+=1
flag=0
for k in range(len(dat)):
    if dat[k]>=2:
        flag+=1

if flag==0:
    print('Perfect')
else:
    print('No')