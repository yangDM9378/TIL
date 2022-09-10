arr=[1,5,4,2,-5,-7]
n=int(input())
def select_sort(arr):
    for i in range(len(arr)-1):
        minind=i
        for j in range(i+1,len(arr)):
            if arr[minind]<arr[j]:
                minind=j
        arr[minind],arr[i]=arr[i],arr[minind]
    return arr
k=select_sort(arr)
print(k[n-1])