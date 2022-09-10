a=int(input())
arr=[+3,+2,-1,+3,-2,999,-1]
def kkk(z):
    if arr[z]==999:
        print(f'{z}번')
        return

    c=z+arr[z]
    kkk(c)
    print(f'{z}번')
kkk(a)