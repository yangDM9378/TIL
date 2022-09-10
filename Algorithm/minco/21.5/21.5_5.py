vect=list(map(int, input().split()))
bucket=[0]*10

for i in range(len(vect)):
    bucket[vect[i]]+=1

for i in range(1,len(bucket)):
    bucket[i]+=bucket[i-1]

result=[0]*10
for i in range(len(vect)):
    index=vect[i]
    result[bucket[index]-1]=vect[i]
    bucket[index]-=1
for i in range(len(vect)):
    print(result[i],end=' ')