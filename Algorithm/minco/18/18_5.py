arr=list(input())
z_arr=[0]*25
for i in range(len(arr)):
    z_arr[ord(arr[i])-65]+=1

temp=0
for j in range(len(z_arr)):
    if temp<z_arr[j]:
        temp=z_arr[j]
        k=j
print(chr(k+65))