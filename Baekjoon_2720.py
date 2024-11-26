def money(C):
    Quarter, Dime, Nickel, Penny = 25, 10, 5, 1
    calculate = [Quarter, Dime, Nickel, Penny]
    change = []
    for i in calculate:
        change.append(C//i)
        C = C - (i*(C//i))
    print_list(change)

def print_list(k):
    for i in k:
        print(i, end=" ")
    print()
    

T = int(input())

for _ in range(T):
    C = int(input())
    money(C)