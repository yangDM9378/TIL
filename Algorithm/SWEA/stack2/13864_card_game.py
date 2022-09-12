T=int(input())
def kkk(k):
    global li
    print(k)
    if len(k)==1:
        li.append(k.pop())
        return
    stack=[]
    while k:
        if len(k) % 2 == 0:
            b = k.pop()
            a = k.pop()
            c = res(a, b)
            stack.append(c)
        else:
            stack.append(k.pop())
            b = k.pop()
            a = k.pop()
            c = res(a, b)
            stack.append(c)

    kkk(stack[::-1])

def res(a,b):
    if a[0]==1:
        if b[0]==1:
            if a[1]<b[1]:
                return a
            else:
                return b
        elif b[0]==2:
            return b
        else:
            return a
    elif a[0]==2:
        if b[0]==1:
            return a
        elif b[0]==2:
            if a[1] < b[1]:
                return a
            else:
                return b
        else:
            return b
    else:
        if b[0]==1:
            return b
        elif b[0]==2:
            return a
        else:
            if a[1] < b[1]:
                return a
            else:
                return b
for t in range(T):
    N=int(input())
    arr=list(map(int, input().split()))
    arr_r=[]
    arr_l=[]
    li=[]
    for i in range(0, (N-1)//2+1):
        arr_l.append([arr[i],i+1])
    for j in range((N-1)//2+1, N):
        arr_r.append([arr[j], j+1])
    kkk(arr_l)
    kkk(arr_r)
    a=li.pop()
    b=li.pop()
    result=res(a,b)
    print(f'#{t+1} {result[1]}')
