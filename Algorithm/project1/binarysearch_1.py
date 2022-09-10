curser=['##########','##########','__________','__________','__________']


def row_sear():
    for i in range(len(curser)):
        if curser[i][0] != '#':
            return i-1


def params(s,e,arr):
    maxx = -1
    while (1):
        m = (s + e) // 2
        if arr[m] == '#':
            maxx = m
            s = m + 1
        elif arr[m] != '#':
            e = m - 1
        if e < s:
            return maxx + 1

i=row_sear()
a=curser[i]
j=params(0,9,a)
print(i,j)