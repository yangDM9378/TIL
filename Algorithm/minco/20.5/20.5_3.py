a=input()

if len(a)%2==1:
    print('다른문장')
else:
    if a[0:len(a)//2]==a[len(a)//2:]:
        print('동일한문장')


    else:
        print('다른문장')