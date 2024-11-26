A, B, V = map(int, input().split())

day_meter = A - B
day = 1

# while (meter < V):
#     meter = meter + A
#     if (meter >= V):
#         break
#     else:
#         meter = meter - B
#     day = day + 1
# 
# print(day)

if (A == V):
    print(day)
else:
    V = V - A
    n = V // day_meter
    if (V % day_meter == 0):
        print(day + n)
    else:
        print(day + n + 1)