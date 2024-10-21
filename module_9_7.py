def is_prime(funk):
    def wrapper(*args, **kwargs):
        result_sum = funk(*args, **kwargs)
        for i in range(2, (result_sum // 2) + 1):
            if result_sum % i == 0:
                print('Составное')
                return result_sum
        print('Простое')
        return result_sum
    return wrapper


@is_prime
def sum_three(*nums):
    a = 0
    for num in nums:
        a += num
    return a


print(sum_three(2, 3, 6))
