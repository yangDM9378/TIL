arr=list(input())
dat=[0]*6
for i in range(len(arr)):
    dat[ord(arr[i])-65]+=1
for j in range(len(dat)):
    if dat[j]>=1:
        print(chr(j+65), end='')