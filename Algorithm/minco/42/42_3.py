import copy
def dfs(now):
    global n
    global word_a
    if word_a==word:
        n=now
        return

    if now==n:
        return

    for i in range(5):
        if used[i]==1:continue
        data_word=copy.deepcopy(word_a)
        used[i]=1
        word_a+=arr[i]
        dfs(now+1)
        used[i]=0
        word_a=data_word

word=input()
arr=['BTS','SBS','BS','CBS','SES']
n=5
path=[]
used=[0]*5
word_a=''
dfs(0)
print(n)