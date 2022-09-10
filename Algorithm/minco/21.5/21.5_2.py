arr=[[3,4,1,5],[3,4,1,3],[5,2,3,6]]
sum_li=[0,0,0,0]

for j in range(4):
    for i in range(3):
        sum_li[j]+=arr[i][j]
a=int(input())
print(sum_li[a])