z=65
re=[]
for k in range(5):
    li = []
    for i in range(z,z+5):
        li.append(chr(i))
    z+=5
    re.append(li)

a=input()
for i in range(5):
    for j in range(5):
        if re[i][j]==a:
            print(f'{i-2},{j-2}')
