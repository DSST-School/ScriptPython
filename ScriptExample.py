def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Ввод от пользователя
n = int(input("Введите количество чисел Фибоначчи: "))

# Печать последовательности
print("Последовательность Фибоначчи:")
print(fibonacci(n))