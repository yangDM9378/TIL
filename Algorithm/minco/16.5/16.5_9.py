a,b,c=map(str, input().split())

for i in range(2):
    for j in range(int(a)):
        for k in range(int(b)):
            print(c, end='')
        print()
    print(end='\n')