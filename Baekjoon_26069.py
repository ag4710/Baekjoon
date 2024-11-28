n = int(input())
a = [input().split() for _ in range(n)]

result = {'ChongChong'}

for arr in a:
    if any(element in arr for element in result):
        result.update([arr[0], arr[1]])

print(len(result))