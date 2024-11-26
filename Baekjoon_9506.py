def divisors(n):
    divisor_list = []
    for i in range(1, n+1):
        if (n % i == 0):
            divisor_list.append(i)
    return divisor_list

while True:
    n = int(input())
    sum_divisors = 0
    if (n == -1):
        break
    
    n_divisors = divisors(n)
    sum_divisors = sum(n_divisors) - n
    
    if (sum_divisors == n):
        print(f'{n} =', end=" ")
        for i in range(0,len(n_divisors)-1):
            print(f'{n_divisors[i]}', end =" ")
            if (i != len(n_divisors)-2):
                print("+", end=" ")
    else:
        print(f'{n} is NOT perfect.', end=" ")
    print()