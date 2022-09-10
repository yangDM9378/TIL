T=int(input())
li=[]
for _ in range(T):
    a=input()
    if a[0].isupper()==1 and a[1:].islower()==1:
        a=a
    elif a.isupper()==1:
        a=a.upper()
    elif a.islower()==1:
        a=a.capitalize()
    else:
        a=a.upper()
    li.append(a)
for i in range(len(li)):
    print(sorted(li)[i])
