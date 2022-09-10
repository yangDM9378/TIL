coin=[100,50,10]

change=int(input())
k=0
# for i in coin:
#     re=change//i
#     change=change%i
#     k+=re
#     print(f'{i}:{re}')
# print(k)

while(1):
     i=0
     re=change//coin[i]
     change=change%coin[i]
     print(re, change)

     if i==3:
         break