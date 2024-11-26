N = int(input())
i = 2
Prime_factors = []

while (i <= N):
    if ((N % i) == 0):
        Prime_factors.append(i)
        N = N // i
    else:
        i = i + 1

for i in Prime_factors:
    print(i)
