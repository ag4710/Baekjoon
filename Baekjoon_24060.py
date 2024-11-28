def merge_sort(A, p, r):
    global count, result
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    i, j, t = p, q + 1, 0
    tmp = [0] * (r - p + 1)

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]

    for i in range(len(tmp)):
        A[p + i] = tmp[i]

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1

merge_sort(A, 0, N - 1)

print(result)