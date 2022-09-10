wor=list('GHOST')
arr=list(input())


def wor_fun(a):
    for j in range(len(wor)):
        if arr[a+j]!=wor[j]:
            return 0
    return 1

flag=0
for i in range(len(arr)-len(wor)+1):
    k=wor_fun(i)
    flag+=k

if flag==1:
    print('존재')
else:
    print('존재하지 않음')