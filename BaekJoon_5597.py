list = []

for _ in range(30):
    list.append(1)

for _ in range(28):
    a = int(input())
    list[a-1] = 0

for i in range(30):
    if (list[i] == 1):
        print(i+1)