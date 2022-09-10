arr=[[3,1,9],[7,2,1],[1,0,8]]
masking=[list(map(int, input().split())) for _ in range(3)]
li=[]
for i in range(3):
    for j in range(3):
        if masking[i][j]==1:
            li.append(arr[i][j])

def re(a):
    for k in a:
        if 3<=k<=5:
            return 1

if re(li)==1:
    print('발견')
else:
    print('미발견')