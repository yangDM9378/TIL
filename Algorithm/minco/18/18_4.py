arr=list(input())

z_li=[0]*25
for i in range(len(arr)):
    z_li[(ord(arr[i])-65)%25]+=1
c=0
for k in range(len(z_li)):
    if z_li[k]!=0:
        c+=1

print(f'{c}개')