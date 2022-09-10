bettery="_______"
arr=list(bettery)

def parametric(s,e):
    maxx = -1
    while (1):
        m=(s+e)//2
        if arr[m]=='*':
            maxx=m
            s=m+1
        elif arr[m]!='*':
            e=m-1
        if e<s:
            return maxx + 1


print((parametric(0,len(arr)-1))*10)