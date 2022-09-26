arr=[500,100,50,10]
cnt=0
money=int(input())
for i in range(4):
    a=money//arr[i]
    cnt+=money//arr[i]
    money=money%arr[i]

print(cnt)