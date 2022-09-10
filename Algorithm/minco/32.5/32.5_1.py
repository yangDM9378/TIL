
word=str(input())
arr=['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']
idx_li=[]
for i in range(len(word)):
    if word[i]!='?':
        idx_li.append(i)
cnt=0
for j in range(len(arr)):
    flag=0
    for i in idx_li:
        if arr[j][i]!=word[i]:
            flag+=1
    if flag==len(idx_li):
        cnt+=1
print(cnt)