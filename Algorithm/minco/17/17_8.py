a=list(map(str, input().split()))
vect=['B','T','K','I','G','Z']
cnt=0
for i in vect:
    for j in range(len(a)):
        if i == a[j]:
            cnt+=1
print(cnt)