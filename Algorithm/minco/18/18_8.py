train=[3,7,6,4,2,9,1,7]
team=list(map(int,input().split()))

for i in range(6):
    flag=0
    for j in range(3):
        if train[i+j]==team[j]:
            flag+=1

    if flag == 3:
        print(f'{i}번~{i+2}번 칸')
