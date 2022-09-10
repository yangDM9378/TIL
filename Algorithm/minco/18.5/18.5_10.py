arr=list(input())
z=[0]*26

for i in range(len(arr)):
    z[ord(arr[i])-65]+=1

for j in range(len(z)):
    if z[j]!=0:
        print(f'{chr(j+65)}:{z[j]}')