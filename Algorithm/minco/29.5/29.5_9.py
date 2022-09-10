a=input()
b=input()
# 자를 단어
def abc(a,b):
    k=len(b)
    for i in range(len(b)-1,-1,-1):
        for m in range(len(b)-i):
            k=b[m:m+i+1]
            if a.count(k)==1:
                return k
print(abc(a,b))