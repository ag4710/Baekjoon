n, m = map(int, input().split())
list = []

for i in range(n):
    list.append(i+1)

for _ in range(m):
    i, j = map(int, input().split())
    list2 = []
    for k in range(j-i+1):
        list2.append(list[i-1+k])
    list2.reverse()
    for q in range(j-i+1):
        list[i-1+q] = list2[q]

for w in list:
    print(w, end=" ")