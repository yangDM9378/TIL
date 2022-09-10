def maxIndex(li):
    temp=65
    for i in range(len(li)):
        if ord(li[i])>=temp:
            temp=ord(li[i])
            result=i
    return result

def minIndex(li):
    temp=125
    for i in range(len(li)):
        if ord(li[i])<=temp:
            temp=ord(li[i])
            result=i
    return result

word_li=list(input())
print(maxIndex(word_li))
print(minIndex(word_li))