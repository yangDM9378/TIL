name=['Amy','Bob','Edger','Diane','Chloe']
arr=[[0,0,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
sum=0
Max=0
Maxindex=0
for j in range(5):
      sum=0
      for i in range(5):
           if arr[i][j]==1:
                 sum+=1
      if sum>Max:
            Max=sum
            Maxindex=j
print(name[Maxindex])