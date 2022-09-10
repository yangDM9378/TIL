a=input()

for i in range(ord(a)-3,ord(a)+4):
    print(chr(65+(i-65)%26), end='')