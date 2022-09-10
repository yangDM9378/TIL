arr=[list(input()) for _ in range(4)]
def a(arr,word):
    for i in range(4):
        for j in range(3):
           if arr[i][j]==word:
               return i,j

print(abs(a(arr,'A')[0]-a(arr,'B')[0])+abs(a(arr,'A')[1]-a(arr,'B')[1]))

