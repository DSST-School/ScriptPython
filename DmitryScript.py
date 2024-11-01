def factorial(n):
    """Вычисляет факториал числа n."""
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif n in (0, 1):
        return 1
    return n * factorial(n - 1)

def main():
    while True:
        try:
            n = int(input("Введите число для вычисления факториала (или 'q' для выхода): "))
            print(f"Факториал {n} равен {factorial(n)}")
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break

if __name__ == "__main__":
    main()
