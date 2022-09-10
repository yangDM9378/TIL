li=[list(input()) for _ in range(3)]
len_li=[0]*3

for i in range(3):
    len_li[i]=len(li[i])

result=[]
for j in range(3):
    if max(len_li)==len_li[j]:
        result.append(li[j])


used=[0]*len(result[0])
li=[]
result_cnt=0
def a(level,arr):
    global li
    global cnt
    global result_cnt
    if level==len(result[0]):
        cnt+=1
        if li==arr:
            result_cnt=cnt
        return

    for i in range(1,-1,-1):
        if used[i]==1:continue
        li.append(wor[i])
        used[i]==1
        a(level+1,arr)
        used[i]=0
        li.pop()

wor=['1','0']
num_li=[]

for k in range(len(result)):
    cnt = 0
    a(0, result[k])
    num_li.append(result_cnt)

temp=0
id=0
for k in range(len(result)):
    if num_li[k]>temp:
        temp=num_li[k]
        id=k

for k in range(len(result[id])):
    print(result[id][k], end='')


