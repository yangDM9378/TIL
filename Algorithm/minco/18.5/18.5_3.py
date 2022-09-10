arr=list(input())
a=[0]*26
for i in range(len(arr)):
    a[ord(arr[i])-65]+=1

temp=a[0]
k=0
for i in range(1,len(a)):
    if a[i]>temp:
        k=i
print(chr(k+65))