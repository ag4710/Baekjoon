import string

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ascii_uppercase_list = list(string.ascii_uppercase)
all_number = number + ascii_uppercase_list

N, B = map(int, input().split())
remain = []
while (N != 0):
    remain.append(N % B)
    N = N//B

for i in remain[::-1]:
    print(all_number[i], end="")