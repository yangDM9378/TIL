arr=[['C', 'D', 'A'],
    ['B', 'M', 'Z'],
    ['Q', 'P', 'O']]

arr1=list(input())
z_li=[0]*26

for i in range(3):
    for j in range(3):
        z_li[ord(arr[i][j])-65]+=1
for k in range(len(arr1)):
    z_li[ord(arr1[k]) - 65] += 1
re=0
for z in range(len(z_li)):
    if z_li[z] >1:
        re+=1
print(f'{re}명')