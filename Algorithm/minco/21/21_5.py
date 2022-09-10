a,b,c=[list(input()) for _ in range(3)]

arr=[]
arr.append(a)
arr.append(b)
arr.append(c)

li=[]
for i in range(3):
    li.append(len(arr[i]))

li_max=max(li)
for j in range(3):
    if len(arr[j])==li_max:
        arr[j],arr[0]=arr[0], arr[j]

for i in range(3):
    for k in range(len(arr[i])):
        print(arr[i][k], end='')
    print()