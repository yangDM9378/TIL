dict1={}
dict2=dict()

burger={'cy':3000,'wp':5000}

# 싸이버거 가격만 출력!
print(burger['cy'])

burger={
    'mst':{'cy':3000,'chips':500},
    'mc':{'bm':5000,'chips':700}
}

# 빅맥 가격만 출력!
print(burger['mc']['bm'])
#맘스터치 칩스 가격 1000원 인상
burger['mst']['chips']=burger['mst']['chips']+1000
print(burger['mst']['chips'])
print(burger['mst'].get('coke','none'))

# 딕셔너리 mst 값 삭제
del(burger['mst'])
print(burger)
# =============================================
#연습문제

#딕셔너리 값 출력하기
burger={
    'mst':{'cy':3000,'chips':500},
    'mc':{'bm':5000,'chips':700}
}

# 출력결과 1
# mst bm
for i in burger.keys():
    print(i, end=' ')
print()
# 출력결과 2
# {'cy':3000,'chips':500}
# {'bm':5000,'chips':700}
for i in burger.values():
    print(i)
# 출력결과 3
# 3000
# 500
# 5000
# 700
for i,j in burger.items():
    for k in j.keys():
        print(burger[i][k])
# 출력결과 4
# mst {'cy': 3000, 'chips': 500}
# mc {'bm': 5000, 'chips': 700}
for i,j in burger.items():
    print(i,j)

# 출력결과 5
# cy 3000
# chips 500
# bm 5000
# chips 700
for i in burger.values():
    for j,k in i.items():
        print(j,k)
# =============================================

# 정렬 후 출력하기
mst={'cy':3000,'chips':500,'coke':300}

# 가격 오름차순 으로 정렬 후 출력하기
# 출력결과
# coke 300
# chips 500
# cy 3000
ret=sorted(mst.items(), key=lambda x:x[1])
for i in ret:
    print(i[0],i[1])

# 가격 내림차순 으로 정렬 후 출력하기
#출력결과
# cy 3000
# chips 500
# coke 300
ret=sorted(mst.items(), key=lambda x:-x[1])
for i in ret:
    print(i[0],i[1])

# 이름 기준으로 오름차순
# 출력결과
# chips 500
# coke 300
# cy 3000
ret=sorted(mst.items(), key=lambda x:x[0])
for i in ret:
    print(i[0],i[1])

# 이름 기준으로 내림차순
# 출력결과
# cy 3000
# coke 300
# chips 500
ret=sorted(mst.items(), key=lambda x:x[0], reverse=True)
for i in ret:
    print(i[0],i[1])

# =============================================
print('------------')
fastfood=[
    {'name':'mst','burger':3000,'chips':500,'tasty':'C'},
    {'name':'mc','burger':5000,'chips':700,'tasty':'A'},
    {'name':'bk','burger':7000,'chips':300,'tasty':'A'},
]
# 맛 오름차순 and 버거가격 내림차순으로 정렬해서 출력하기
ret=sorted(fastfood, key=lambda x:(x['tasty'],-x['burger']))
for i in ret:
    print(i)