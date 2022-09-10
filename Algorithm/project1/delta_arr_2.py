N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
Max=int(-21e8)
dy,dx=0,0

def getSum(y,x):  # 전달받은 좌표값 기준으로 sum 구한 후
    sum=0
    for i in range(2):
        for j in range(3):
            sum+=arr[i+y][j+x]
    return sum  # 구한 sum 리턴

for i in range(2):
    for j in range(3):
        ret=getSum(i,j)  # 0,0 부터 1,2 까지 좌표값 전달
        if ret>Max: # 리턴받은값 갱신
            Max=ret
            dy=i
            dx=j
print(Max)  # 최대값과
print(dy,dx) # 그 좌표값 까지 출력