diry=[-1,1,0,0]
dirx=[0,0,1,-1]
arr=[['_','_','_'],['_','_','_'],['A','T','K'],['_','_','_'],['_','_','_']]
def search_word(word):
    for y in range(5):
        for x in range(3):
            if arr[y][x]==word:
                return y,x

for _ in range(7):
    word, dirct=map(str, input().split())
    if dirct=='UP':
        y,x=search_word(word)
        dy=y+diry[0]
        dx=x+dirx[0]
        arr[dy][dx],arr[y][x]=arr[y][x],arr[dy][dx]
    elif dirct=='DOWN':
        y, x = search_word(word)
        dy=y+diry[1]
        dx=x+dirx[1]
        arr[dy][dx],arr[y][x]=arr[y][x],arr[dy][dx]

    elif dirct=='RIGHT':
        y, x = search_word(word)
        dy=y+diry[2]
        dx=x+dirx[2]
        arr[dy][dx],arr[y][x]=arr[y][x],arr[dy][dx]

    else:
        y, x = search_word(word)
        dy=y+diry[3]
        dx=x+dirx[3]
        arr[dy][dx],arr[y][x]=arr[y][x],arr[dy][dx]

for i in range(5):
    for j in range(3):
        print(arr[i][j], end='')
    print()