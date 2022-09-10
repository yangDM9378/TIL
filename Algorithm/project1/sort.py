# selection sort
# 선택정렬
# O(n^2)
# 구현쉽다 느리다
arr=[4,7,1,3,5,2]
for y in range(len(arr)-1):
    for x in range(y+1,len(arr)):
        if arr[y]>arr[x]:
            temp=arr[y]
            arr[y]=arr[x]
            arr[x]=temp

# insert sort
# 삽입정렬
# O(n^2)
# 느리다
arr=[4,7,1,3,5,2]
result=[]
for i in range(len(arr)):
    result.append(arr[i])
    for j in range(i,0,-1):
        if result[j-1]>result[j]:
            result[j],result[j-1]=result[j-1],result[j]
        else:
            break

# Direct Addressing Table
# 빠른 검색, 양의 정수값만 가능
# 메모리를 비효율적으로 탐색
a=[4,7,1,3,4,1,2,4]
b=[3,2,5,4]
bucket=[0]*len(a)
for i in a:
    bucket[i]+=1
for k in b:
    print(f'{k}:{bucket[k]}')


# 계수정렬(counting sort)
n=int(input())
a=list(map(int,input().split()))
bucket=[0]*101
# dat 등록
for i in range(n):
    bucket[a[i]]+=1
# 누적합 구하기
for i in range(1,len(bucket)):
    bucket[i]+=bucket[i-1]
    # bucket[i]=bucket[i]+bucket[i-1]
# 값넣기
result=[0]*101
for i in range(n):
    index=a[i]
    result[bucket[index]-1]=a[i]
    bucket[index]-=1
for i in range(n):
    print(result[i],end=' ')