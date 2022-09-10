arr=list(input())
n=int(input())
arr.sort()
arr=arr[-n:]
dic_arr={}
for i in range(len(arr)):
    dic_arr[arr[i]]=arr.count(arr[i])
sorted_dict=sorted(dic_arr.items(), key=lambda item: item[1], reverse=False)
print(sorted_dict[-1][0])