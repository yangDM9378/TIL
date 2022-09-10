
def a(word):
    for i in range(len(word)):
        print(word[i], end='')
    print()
    if word==['_']*k:
        return

    for i in range(len(word)):
        if ord(word[i]) - 1 == 64:
            word[i] = '_'
        elif 65<=ord(word[i]) - 1<=91:
            word[i]=chr(ord(word[i])-1)
        else:
            word[i]=word[i]

    return a(word)


word=list(input())
k=len(word)
a(word)