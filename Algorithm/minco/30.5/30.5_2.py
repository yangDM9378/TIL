def dfs(now, level):
    global li
    if level==n:
        for k in range(level):
            print(li[k], end='')
        print()
        return

    for i in range(2):
        li.append(arr[i])
        dfs(i,level+1)
        li.pop()
n=int(input())
li=[]
arr=['o','x']
dfs(0,0)