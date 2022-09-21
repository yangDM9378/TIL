def bfs(s,e):
    global Min
    q=deque()
    q.append([s,0])
    while q:
        node=q.popleft()
        nows, level=node[0], node[1]

        if nows==e:
            return level

        copy_s=nows
        nows=nows//2
        if 0<=nows<100000 and used[nows]==0:
            q.append([nows,level+1])
        used[nows]=1
        nows=copy_s

        nows=nows*2
        if 0<=nows<100000 and used[nows]==0:
            q.append([nows,level+1])
            used[nows]=1
        nows=int(nows/2)

        nows=nows+1
        if 0<=nows<100000 and used[nows]==0:
            q.append([nows,level+1])
            used[nows]=1
        nows-=1

        nows=nows-1
        if 0<=nows<100000 and used[nows]==0:
            q.append([nows,level+1])
            used[nows]=1




from collections import deque
s=int(input())
e=int(input())
used=[0]*100001
used[s]=1
print(bfs(s,e))
