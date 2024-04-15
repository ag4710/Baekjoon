x = int(input())
y = x
num = 1

while True:
    y = y - num
    if (y <= 0):
        break
    num = num + 1

if num % 2 == 0:
    if num == num or (num-y) == 1:
        print(f"{num+y}/{(num+1)-(num+y)}")
    else:
        print(f"{(num+1)-(num+y)}/{num+y}")
else:
    if num == num or (num-y) == 1:
        print(f"{(num+1)-(num+y)}/{num+y}")
    else:
        print(f"{num+y}/{(num+1)-(num+y)}")