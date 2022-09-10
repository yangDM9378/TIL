a=list(map(int,input().split()))
b=list(map(int, input().split()))
z=[0]*8
s = 0
e = 0
i=0
while 1:
    if s>3 and e>3:
        break
    if s>3 or e>3:
        if s>3:
            z[i]=b[e]
            i+=1
            e+=1
        else:
            z[i]=a[s]
            i+=1
            s+=1
    else:
        if a[s]<=b[e]:
            z[i]=a[s]
            s+=1
            i+=1
        else:
            z[i]=b[e]
            e+=1
            i+=1
print(*z)