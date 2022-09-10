n=int(input())
arr=[[0]*n for _ in range(n)]
#1
cnt=1
for j in range(n):
    for k in range(n):
        arr[k][j]=cnt
        cnt+=1
print(arr)

#2
cnt=1
for j in range(n):
    for k in range(n):
        arr[2-k][2-j]=cnt
        cnt+=1
print(arr)
#3
cnt=1
for j in range(n):
    for k in range(n):
        if j%2==0:
            arr[j][k]=cnt
            cnt+=1
        else:
            arr[j][2-k]=cnt
            cnt+=1

print(arr)

#4
arr=[[0]*n for _ in range(n)]
cnt=1
sum=0
for j in range(n):
    for k in range(n):
        if
        arr[j][k]=cnt
        cnt+=1