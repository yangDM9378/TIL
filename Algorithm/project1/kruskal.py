# minimum spanning tree(최소신장트리)를 해결하는 크루스칼 알고리즘
# 5
# 8
# C D 1
# A C 3
# C E 5
# A E 7
# A B 9
# B D 11
# B C 14
# A D 20

def findboss(member):
    if arr[ord(member)]==0:
        return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(y,x):
    global answer,cnt
    yboss,xboss=findboss(y),findboss(x)
    if yboss==xboss: return
    answer+=i[0]     # 비용 더하기
    cnt+=1           # 간선의개수 더하기
    arr[ord(xboss)]=yboss


k=int(input()) # 정점개수
n=int(input()) # 간선개수
# 간선의 정보 입력
lst=[]
for i in range(n):
    a, b, cost = map(str, input().split())
    z=[int(cost), a, b]
    lst.append(z)
lst.sort()
arr=[0]*200

answer=0 # 비용을 더할 변수
cnt=0    # 간선의 개수를 더할 변수
for i in lst:
    if cnt==k-1:     # cnt가 간선의 개수 -1 개와 같으면
        print(answer)
        break
    union(i[1],i[2])
    print(arr)
