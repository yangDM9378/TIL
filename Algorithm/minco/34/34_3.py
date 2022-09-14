def binary_search(s,l,n,S):
    while 1:
        global cnt
        cnt += 1
        m=(s+l)//2
        if arr[m]==n:
            return 1

        if len(arr[m]) < len(n):
            len_min=len(arr[m])
        else:
            len_min=len(n)

        for i in range(len_min):
            if ord(arr[m][i])==ord(n[i]):continue

            if ord(arr[m][i]) > ord(n[i]):
                l=m-1
                break
            elif ord(arr[m][i]) < ord(n[i]):
                s=m+1
                break

        if cnt>=int(S):
            return 0
        if s>l:
            return 0


T=int(input())
arr=list(map(str, input().split()))
arr=sorted(arr)

M=int(input())
for _ in range(M):
    n, S = map(str, input().split())
    cnt=0
    ret=binary_search(0, len(arr)-1, n, S)
    if ret ==0:
        print('fail')
    else:
        print('pass')
