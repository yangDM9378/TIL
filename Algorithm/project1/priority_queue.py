# import heapq # 우선순위 큐를 사용하기 위한 모듈
#
# arr=[] # 모듈함수를 사용할때 이 arr 리스트에 인자갑슬 담을 것이다.
# heapq.heappush(arr,4)
# heapq.heappush(arr,15)
# heapq.heappush(arr,2)
# heapq.heappush(arr,7)
# heapq.heappush(arr,5)
# heapq.heappush(arr,9)
# print(arr)
# print(heapq.heappop(arr)) # log n 속도로 우선순위가 높은 값을 출력
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# for i in range(len(arr)):
#     print(heapq.heappop(arr),end=' ')
# print()
# print('------')
# import heapq
# arr=[4,87,4,24,8,23,3,7,4]    # pq 사용하여 최소값 부터 출력이 되도록 코드 적어보기
# heapq.heapify(arr) # arr 리스트를 한번에 heap 자료형을 바꾸기
# for i in range(len(arr)):
#     print(heapq.heappop(arr), end=' ')
# heap=[] # heap 리스트에 arr 요소의 값을 heap 자료형으로 저장하기 위함
# for i in range(len(arr)):
#     heapq.heappush(heap,arr[i])
#
# for i in range(len(arr)):
#     print(heapq.heappop(heap))


# maxheap
# import heapq
# arr=[4,87,4,2,4,6,8,7]
# heap=[]
# #1
# for i in range(len(arr)):
#     heapq.heappush(heap, (-arr[i]))
# for i in range(len(arr)):
#     print(heapq.heappop(heap)*-1, end=' ')
#     # print(-heapq.heappop(heap), end=' ')
# #2 람다사용
# vect=[3,6,3,1,7,9]
# rev=lambda x:x*-1
# heap1=list(map(rev,vect))
# heapq.heapify(heap1)
# for i in range(len(vect)):
#     print(-heapq.heappop(heap1))
# #3 튜플
# for i in range(len(arr)):
#     heapq.heappush(heap,(-arr[i],arr[i]))
# for i in range(len(arr)):
#     print(heapq.heappop(heap)[1], end=' ')












