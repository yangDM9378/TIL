from collections import Counter

a=[1,1,1,1,2,3,4]
b=[1,1,2,3]

print(Counter(a))
print(Counter(b))
print(Counter(a)-Counter(b))
c=Counter(a)-Counter(b)
print(list(c.items())[0])

def solution(participant, completion):
    c=Counter(participant)-Counter(completion)
    answer=list(c.items())[0][0]
    return answer

participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
c=solution(participant,completion)
print(c)
