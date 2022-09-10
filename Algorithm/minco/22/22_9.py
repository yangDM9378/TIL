arr=['Jason', 'Dr.tom','EXEXI','GK12P','POW']
word=input()
def abc(lev):
    if lev==4:
        print('암호틀림')
        return
    if word == arr[lev]:
        print('암호해제')
        return
    abc(lev+1)


abc(0)