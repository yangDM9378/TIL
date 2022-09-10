arr=[['A','T','K','B'],['C','Z','F','D'],['H','G','E','I']]

a,b,c=map(str, input().split())
for i in range(3):
    for j in range(4):
        if arr[i][j]==a:
            print(arr[i+int(b)][j+int(c)])