arr=[[0]*4 for i in range(7)]
k=1

for i in range(7):
    for j in range(4):
        arr[i][j]=k
        k+=1
li=list(map(int, input().split()))
for li_n in li:
    arr[li_n]=[0]*4

for i in range(7):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()