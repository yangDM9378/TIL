a,b=map(int, input().split())
arr=[[] for _ in range(a)]
for _ in range(b):
    i, name=map(str,input().split())
    i=int(i)
    arr[i].append(name)
li=[]
for i in range(a):
    li.append(len(arr[i]))
max_len=max(li)
def aaa():
    for i in range(a):
        if max_len==len(arr[i]):
            return i

print(*arr[aaa()])