num = []
max = 0
index = 10

for i in range(9):
    a = int(input())
    num.append(a)

    if (max < a):
        max = a
        index = i + 1

print(max)
print(index)