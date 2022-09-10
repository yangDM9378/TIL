arr = list(map(int,input().split()))
path = []
cnt = 0
sum = 0
def abc(level):
    global cnt
    global path
    global sum

    sum = 0

    for i in range(level):
        sum += path[i]
    if sum >= 10 and 20 >= sum:
        cnt += 1

    if level == len(arr):
        return

    for i in range(len(arr)):
        if level>0 and path[level-1] >= arr[i]:continue
        path.append(arr[i])
        abc(level+1)
        path.pop()

abc(0)
print(cnt)