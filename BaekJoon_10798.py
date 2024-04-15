tot_list = [[None for _ in range(15)] for _ in range(5)]

for i in range(5):
    a = list(input())
    for j in range(len(a)):
        tot_list[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if (tot_list[j][i] != None):
            print(tot_list[j][i], end="")
