arr=[[3,5,4],[1,1,2],[1,3,9]]
a=[-1,1,0,0]
b=[0,0,1,-1]
x,y=map(int,input().split())
sum_arr=0
for i in range(4):
    dx=x+a[i]
    dy=y+b[i]
    if dx<0 or dx>2 or dy<0 or dx>2:
        continue
    sum_arr+=arr[dx][dy]
print(sum_arr)