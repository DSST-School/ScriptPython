def factorial(n):
    if n < 0:
        return "Факториал не определен для отрицательных чисел."
    elif n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Введите число для вычисления факториала: "))
        print(f"Факториал {n} равен {factorial(n)}")
    except ValueError:
        print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
