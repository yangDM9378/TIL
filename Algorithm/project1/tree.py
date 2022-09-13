# Tree
## 트리의 순회(탐색하면서 출력순서)
### 전위 preorder
### 후위 postorder
### 중위 inorder

## 이진트리
### - 1차원배열로 저장가능
#### 전위
arr=' ABCDEFG'
def preorder(now):
    if now>len(arr)-1:
        return
    print(arr[now], end=' ')
    preorder(now*2)
    preorder(now*2+1)
preorder(1)
print()
#### 후위
def postorder(now):
    if now>len(arr)-1:
        return
    postorder(now*2)
    postorder(now*2+1)
    print(arr[now], end=' ')
postorder(1)
print()
#### 중위
def inorder(now):
    if now>len(arr)-1:
        return
    inorder(now*2)
    print(arr[now], end=' ')
    inorder(now*2+1)
inorder(1)

'''
정점번호 V=1~(E+1)
간선수
부모-자식순
4
1 2 1 3 3 4 3 5
'''

E=int(input())
arr=list(map(int, input().split()))
V=E+1
# 부모를 인덱스로 자식 번호 저장
ch1=[0]*(V+1)
ch2=[0]*(V+1)
for i in range(E):
    p,c=arr[i*2], arr[i*2+1]
    if ch1[p]==0:
        ch1[p]=c
    else:
        ch2[p]=c
print(ch1)
print(ch2)