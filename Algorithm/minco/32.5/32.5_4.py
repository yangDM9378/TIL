T=int(input())
arr=[]
for i in range(T):
    a,b = map(str, input().split())
    arr.append([int(a),b])


def a():
    li=[]
    s = 1
    e = 50
    for i in range(len(arr)):
        if arr[i][0] > e or arr[i][0]<s:
            return 'ERROR'
        elif arr[i][1]=='DOWN':
            e = arr[i][0] - 1
        elif arr[i][1]=='UP':
            s = arr[i][0] + 1
    if s==e:
        return f'{s}'
    return f'{s} ~ {e}'
print(a())