a_st='MINCODING'
a=list(a_st)
z=[0]*26#65
N=int(input())
arr=list(map(str,input().split()))


for i in range(len(a)):
    z[ord(a[i])-65]+=1

for j in range(N):
    if z[ord(arr[j])-65]!=0:
        print('O', end='')
        continue
    print('X', end='')