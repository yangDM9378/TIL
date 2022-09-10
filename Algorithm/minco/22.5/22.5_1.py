arr=[[['A','T','B'],['C','C','B']],[['A','A','A'],['B','B','C']]]
N=input()
def abc(arr):
    for i in range(2):
        for j in range(2):
            for k in range(3):
                if arr[i][j][k]==N:
                    return 1

if abc(arr)==1:
    print('발견')
else:
    print('미발견')