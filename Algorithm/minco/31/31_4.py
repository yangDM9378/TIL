arr= [list(input()) for _ in range(5)]
char_arr=['M','A','P','O','M']
def a():
    for j in range(5):
        if arr[j] == char_arr:
            return 'yes'
    return 'no'

for i in range(5):
    arr[i][1],arr[i][3]=arr[i][3],arr[i][1]

print(a())