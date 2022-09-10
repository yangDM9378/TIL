a=input()
for i in range(1,len(a)+1):
    k=a[:i]
    for j in k:
        print(j, end='')
    print()