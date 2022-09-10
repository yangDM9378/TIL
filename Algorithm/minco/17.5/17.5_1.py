startlndex=int(input())

def getSum(startIndex):
    arr = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]
    k=0
    if startIndex<=5:
        for i in range(startIndex, startIndex+5):
            k+=arr[i]
        return k
    else:
        for j in range(startIndex, len(arr)):
            k += arr[j]
        return k

print(getSum(startlndex))