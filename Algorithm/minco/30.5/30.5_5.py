arr=list(input())
n=int(input())
used=[0]*4
li=[]
def a(level):
    global li
    if level==n:
        for i in range(n):
            print(li[i],end='')
        print()
        return

    for i in range(len(arr)):
        if used[i]==1:continue
        used[i]==1
        li.append(arr[i])
        a(level+1)
        used[i]==0
        li.pop()
a(0)