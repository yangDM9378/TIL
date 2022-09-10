vect=[3,5,4,2,6,6,5]
bit_arr=list(map(int, input().split()))

for i in range(len(vect)):
    if bit_arr[i]==1:
        vect[i]=7
    else:
        vect[i]=0
for k in vect:
    print(k, end='')