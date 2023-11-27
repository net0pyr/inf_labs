from sympy import primerange

# Найти все простые числа в диапазоне от 1 до достаточно большого числа (например, 10^7)
primes = list(primerange(1, 10**7))

# Получить 600,000-е простое число
required_prime = primes[599999]

print(required_prime)
