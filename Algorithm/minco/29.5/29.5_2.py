evid=[-1,0,0,1,2,4,4]
timeStamp=[8,3,5,6,8,9,10]
def crim(a):

    if evid[a]==-1:
        print(f'{a}번index(출발)')
        return

    time=timeStamp[a]
    crim(evid[a])
    print(f'{a}번index({time}시)')


n=int(input())
crim(n)