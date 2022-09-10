arr=[
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

def bfs(now):
    queue=[now]
    while queue:
        node=queue.pop(0)
        print(node, end=' ')
        for i in range(len(arr[node])):
            if arr[node][i]==1:
                queue.append(i)

n=int(input())
bfs(n)