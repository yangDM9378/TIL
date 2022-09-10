li=[['A','B','K','T'],['K','F','C','F'],['B','B','Q','Q'],['T','P','Z','F']]
a=list(map(str,input().split()))
num=0
for i in li:
    for j in i:
        if j in a:
            num+=1
print(num)