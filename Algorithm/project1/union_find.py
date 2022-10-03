# union find 자료구조
# 각각의 독립되 data를 그룹화 시켜 자료들을 관리할때 사용하는 자료구조
def findboss(member):
    global arr
    if arr[ord(member)]==0: # 매개변수에 해당하는 곳의 값이 0이라면
        return member       # 자기 자신이 보스!!
    ret=findboss(arr[ord(member)]) # 배열에 적혀있는 값으로 다시 보스 찾아보기
    return ret

def union(a,b):
    global arr
    aboss=findboss(a)  # boss 찾기
    bboss=findboss(b)
    if aboss==bboss:  # boss가 같다 -> 이미 같은 그룹
        return
    arr[ord(bboss)]=aboss  # 두보스가 다르다면 b의 보스에 해당하는 값에 a의 보스적기

arr=[0]*200
union('A','B') # 두 그룹을 하나의 그룹으로
union('D','E') # 합쳐주는 함수
union('B','E')
union('B','D')
union('F','E')

y,x=input().split()
if findboss(y)==findboss(x):
    print("같은그룹")
else:
    print("다른그룹")




# # 사이클 존재여부파악
# n=int(input())
# edge=[]
# for _ in range(n):
#     edge.append(input().split())

# arr=[0]*200

# def findboss(member):
#     global arr
#     if arr[ord(member)]==0:
#         return member
#     ret=findboss(arr[ord(member)])
#     arr[ord(member)]=ret
#     return ret


# # union 함수
# def union(a,b):
#     global arr

#     fa,fb=findboss(a),findboss(b)
#     if fa==fb:return 1
#     arr[ord(fb)]=fa

# answer=0
# for i in range(n):
#     a,b=edge[i]
#     ret=union(a,b)
#     if ret==1:
#         answer=1
#         break
# if answer:print("cycle 발견")
# else: print("cyccle 미발견")


# Union find (숫자)
def find(node):
    global parents
    if parents[node] == node:
        return node
    ret = find(parents[node]) # 재귀적으로 부모 노드 탐색
    parents[node] = ret # 부모 노드 갱신
    return ret # 부모 노드 반환

def union(a, b):
    global parents
    p_a, p_b = find(a), find(b)
    if p_a == p_b: return True # 부모가 같은 경우 True(사이클 존재)
    parents[p_b] = p_a


n = int(input()) # 간선 갯수
edge = [list(map(int, input().split())) for _ in range(n)] # 간선 정보
parents = list(range(3)) # 각 노드의 부모를 자기 자신으로 초기화

for i in range(n):
    a, b = edge[i]
    if union(a,b):
        print("사이클 발견")
        break
else:
    print("미발견")