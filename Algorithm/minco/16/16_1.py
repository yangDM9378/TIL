col, row= 3,10
li=[[0 for _ in range(row)] for _ in range(col)]
for k in range(3):
  a=list(input())
  for i in range(len(a)):
      li[k][i]=a[i]

result=''
for i in range(3):
    for j in range(9,-1,-1):
        if li[i][j]!=0:
            a=li[i][j]
            result+=a
            break
print(result)