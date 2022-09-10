arr=[[[0]*3 for _ in range(3)] for _ in range(3)]
N=input()
n_ord=ord(N)
for z in range(3):
    for k in range(3):
        for j in range(3):
            arr[z][k][j]=chr(n_ord+z)
for i in range(3):
    for k in range(3):
        for j in range(3):
            print(arr[i][k][j], end='')
        print()
    print()