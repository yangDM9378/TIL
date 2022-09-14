arr=list(input())

s=0
l=len(arr)-1
def parametric_search(s,l):
    maxx=-1
    while 1:
        m=(s+l)//2
        if arr[m]=='#':
            maxx=m
            s=m+1
        elif arr[m]!='#':
            l=m-1
        if l<s:
            return maxx+1

print(f'{parametric_search(s,l)*10}%')