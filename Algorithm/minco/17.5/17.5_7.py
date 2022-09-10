levelTable=[[10,20],[30,60],[100,150],[200,300]]
a=list(map(int, input().split()))
box=[0]*4
for i in range(len(a)):
    if 10<=a[i]<=20:
        box[0]+=1
    elif 30<=a[i]<=60:
        box[1]+=1
    elif 100<=a[i]<=150:
        box[2]+=1
    else:
        box[3]+=1
for i in range(4):
    print(f'lev{i}:{box[i]}')