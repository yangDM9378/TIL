a,b = map(str, input().split())
arr=[[3,5,4,2,2,3],[1,3,3,3,4,2],[5,4,4,2,3,5]]
price=['T','P','G','K','C']
a=ord(a)-65
k=arr[a][int(b)-1]
print(price[k-1])