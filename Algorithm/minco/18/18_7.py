arr= [
    ['A', 'B', 'C'],
    ['A', 'G', 'H'],
    ['H', 'I', 'J'],
    ['K', 'A', 'B'],
    ['A', 'B', 'C']
]
z_arr=[0]*26
for i in range(5):
    for j in range(3):
        z_arr[ord(arr[i][j])-65]+=1

for k in range(len(z_arr)):
    print(chr(k+65)*z_arr[k], end='')