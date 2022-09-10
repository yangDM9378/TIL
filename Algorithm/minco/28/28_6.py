words=list(input())
arr=[list(map(int, input().split())) for _ in range(len(words))]
li=[]

def dfs(now):
    global li
    li.append(words[now])
    for i in range(len(words)):
        if arr[now][i]==1:

            dfs(i)

dfs(0)
for i in li:
    print(i, end='')