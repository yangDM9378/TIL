def dlehd(arr):
    #상하좌우 이동
    dirxy=[[1,0],[-1,0],[0,-1],[0,1]]
    for z in range(len(arr)):
        if arr[z][0] == 0 or arr[z][0] == N-1 or arr[z][1] == 0 or arr[z][1] == N-1:
            arr[z][2]=arr[z][2]//2



T=int(input())

for t in range(T):
    N,M,K=map(int, input().split())
    arr=[]
    for i in range(K):
        a=list(map(int, input().split()))
        arr.append(a)
    print(arr)

