arr=[list(input()) for _ in range(4)]
for k in range(3):
    for i in range(3,-1,-1):
        for j in range(2,-1,-1):
            if arr[i][j]!='_':
                if (i+1)<4:
                    if arr[i+1][j]=='_':
                        arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
for i in range(4):
    for j in range(3):
        print(arr[i][j], end='')
    print()