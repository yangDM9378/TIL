arr=[list(input()) for _ in range(4)]
arr1=[['A','B','C','D'],['B','B','A','B'],['C','B','A','C'],['B','A','A','A']]
li=[]
for i in range(4):
    for j in range(4):
        if arr[i][j]==arr1[i][j]:
            li.append(arr[i][j])

a=0
for i in range(len(li)):
    if a<li.count(li[i]):
        a=li.count(li[i])
        max_i=i
print(li[max_i])