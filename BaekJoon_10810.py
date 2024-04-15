n, m = map(int, input().split())
num = []

for _ in range(n):
    num.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for o in range(j-i+1):
        num[i+o-1] = k

for p in range(n):
    print(num[p], end=" ")