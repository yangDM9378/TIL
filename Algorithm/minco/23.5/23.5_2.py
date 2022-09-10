a_li=[]
b_li=[]
for _ in range(3):
    a,b=map(int, input().split())
    a_li.append(a)
    b_li.append(b)
def abc(a_li, b_li):
    if a_li[0]==a_li[1] or a_li[1]==a_li[2] or a_li[0]==a_li[2]:
        return 1
    if b_li[0]==b_li[1] or b_li[1]==b_li[2] or b_li[0]==b_li[2]:
        return 1

if abc(a_li, b_li)==1:
    print('위험')
else:
    print('안전')