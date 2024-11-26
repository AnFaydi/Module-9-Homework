def is_prime(func):
    def wrapper(a,b,c):
        func_sum = func(a,b,c)
        for i in range(2, func_sum):
            if func_sum % i == 0:
                print('Составное')
                return func_sum
        print('Простое')
        return func_sum
    return wrapper

@is_prime
def sum_three(a,b,c):
    sum = a + b + c
    return sum

result = sum_three(4,0,0)
print(result)