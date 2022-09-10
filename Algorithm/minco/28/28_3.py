name=['A','B','H','C','D','G','E','F']
arr=[[0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

word=input()
name.index(word)
bro=[]

if word=='A':
    print('없음')

else:
    for j in range(len(name)):
        if arr[j][2]==1:
            um=j

    for i in range(len(name)):
        if arr[um][i]==1:
            bro.append(i)
    for i in bro:
        if name[i]!=word:
            print(name[i], end=' ')