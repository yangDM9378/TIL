pw=list(map(int, input().split()))
re=[3,7,4,9]

def isSame(pw, re):
    for i in range(4):
        if re[i]!=pw[i]:
            return 'fail'
    return 'pass'

print(isSame(pw, re))