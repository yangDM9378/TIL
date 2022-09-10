vect=[[3,7,4],[2,2,4],[2,2,5]]
tar=list(map(int, input().split()))
a=[0]*7
for i in range(3):
    for j in range(3):
        for k in tar:
            if vect[i][j]==k:
                a[k]+=1

for z in range(len(a)):
    if a[z] == max(a):
        print(z)