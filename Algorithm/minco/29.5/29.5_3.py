arr=[list(map(int, input().split())) for _ in range(3)]
def aaa(i):
    if arr[i][0]==arr[i][1] and arr[i][1]==arr[i][2]:
        return arr[i][1]
    return 'x'

for i in range(len(arr)):
    print(aaa(i))