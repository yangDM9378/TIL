arr=[5,9,4,6,1,5,8,9]
a,b = map(int, input().split())
k=0
for i in range(a, len(arr)):
   if arr[i]==b:
       print(k)
       break
   k+=1