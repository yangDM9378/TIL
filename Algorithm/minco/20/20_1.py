n = int(input())


def k(n):
    print(n, end=' ')
    if n == 0:
        return

    k(n - 1)
    print(n, end=' ')

k(n)