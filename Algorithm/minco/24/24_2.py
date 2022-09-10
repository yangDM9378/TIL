a=input()
T=int(input())
for _ in range(T):
  word=input()
  word=word.replace(a,'#')
  flag=0
  for i in word:
    if i=='#':
      flag+=1
  if flag==0:
    print('X')
  else:
    print('O')