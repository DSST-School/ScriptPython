def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Ввод от пользователя
n = int(input("Введите предел для поиска простых чисел: "))

# Нахождение и вывод простых чисел
print("Простые числа:", find_primes(n))