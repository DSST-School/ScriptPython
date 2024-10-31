def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 и 1 не являются простыми числами
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

# Ввод от пользователя
n = int(input("Введите предел для поиска простых чисел: "))

# Нахождение и вывод простых чисел
print("Простые числа:", sieve_of_eratosthenes(n))
