arr=[3,5,1,9,7]
z=[0]*5
for _ in range(4):
    w=input()
    if w=='R':
        for i in range(5):
            z[(i+1)%5]=arr[i]
        arr=z[:]

    else:
        for i in range(5):
            z[i-1]=arr[i]
        arr=z[:]


for i in range(5):
    print(z[i], end=' ')