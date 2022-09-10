# T=int(input())
#
# def dfs(N,a):
#     global cnt
#     if a>N:
#         return
#     if a==N:
#         cnt+=1
#         return
#     for i in range(3):
#         dfs(N,a+arr[i])
#
# for t in range(T):
#     N=int(input())
#     arr = [10, 20, 20]
#     cnt=0
#     dfs(N,0)
#     print(f'#{t+1} {cnt}')

T=int(input())

def dfs(N,a):
    global cnt
    if a>N:
        return
    if a==N:
        cnt+=1
        return
    for i in range(3):
        dfs(N,a+arr[i])

for t in range(T):
    N=int(input())
    arr = [10, 20, 20]
    cnt=0
    dfs(N,0)
    print(f'#{t+1} {cnt}')
