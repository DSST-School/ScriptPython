import random
import string

def generate_password(length):
    # Задаем набор символов: буквы, цифры и специальные символы
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерируем пароль заданной длины
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ввод от пользователя
length = int(input("Введите длину пароля: "))

# Генерация и вывод пароля
print("Сгенерированный пароль:", generate_password(length))
