str_a='ATKPTCABC'
li_a=list(str_a)
a,b =map(str, input().split())

def search_a(a):
    for i in range(len(li_a)):
        if li_a[i]==a:
            return i
def search_b(b):
    for j in range(len(li_a)):
        if li_a[len(li_a)-1-j]==b:
            return len(li_a)-j-1

print(search_b(b)-search_a(a))


