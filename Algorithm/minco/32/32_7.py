T=int(input())
arr=[list(map(int, input().split())) for _ in range(T)]
n=int(input())
li=list(map(int, input().split()))
z=[]
for i in range(T):
    for j in range(3):
        if arr[i][j]!=0:
            z.append(arr[i][j])

for j in range(n):
    for i in range(len(z)):
        # print(f'z[i] = {z[i]} / li[j] = {li[j]}')
        if (z[i]%10-li[j])>0:
            z[i]=z[i]-li[j]
        elif (z[i]%10-li[j])<=0:
            z[i]=z[i]//10
        # print(z)



a=''
for k in range(len(z)):
    if z[k]!=0:
        a+=str(z[k])
print(len(a))