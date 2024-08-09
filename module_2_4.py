# Задача "Всё не так уж просто"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    for i in range (2, len(numbers)-1):
        if num % i == 0 and num // i != 1:
            not_primes.append (num)
            break
        elif num % i == 0 and num // i == 1:
            primes.append (num)
            break

print ('primes ', primes)
print ('not_primes ', not_primes)