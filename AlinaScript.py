def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    # Используем массив для хранения статуса простоты чисел
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 и 1 не простые числа
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:  # Если i простое
            # Начинаем с i * i, т.к. все меньшие кратные уже отмечены
            for j in range(i * i, n + 1, i):
                primes[j] = False
    # Возвращаем список простых чисел
    return [i for i in range(n + 1) if primes[i]]

# Ввод от пользователя
try:
    n = int(input("Введите предел для поиска простых чисел: "))
    if n < 0:
        raise ValueError("Предел должен быть неотрицательным.")
    
    # Нахождение и вывод простых чисел
    print("Простые числа:", sieve_of_eratosthenes(n))

except ValueError as e:
    print(f"Ошибка ввода: {e}")
