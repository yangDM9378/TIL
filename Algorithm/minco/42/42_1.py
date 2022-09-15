arr=list(input())
li=[]
def dfs(now,start):
    if now==3:
        for i in range(3):
            print(li[i], end='')
        print()
        return

    for i in range(start,len(arr)):
        li.append(arr[i])
        dfs(now+1,i)
        li.pop()
dfs(0,0)