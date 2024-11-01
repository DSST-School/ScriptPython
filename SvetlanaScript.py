import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Проверка наличия хотя бы одного типа символов
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("Должен быть выбран хотя бы один тип символов.")

    # Собираем доступные символы
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Генерация пароля
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Заполняем оставшуюся длину пароля
    password += random.choices(characters, k=length - len(password))
    
    # Перемешиваем пароль, чтобы случайные символы не были в начале
    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Введите длину пароля (больше 0): "))
            if length <= 0:
                raise ValueError("Длина пароля должна быть положительным числом.")
            break
        except ValueError as e:
            print(e)

    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_lowercase = input("Использовать строчные буквы? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'

    # Генерация и вывод пароля
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print("Сгенерированный пароль:", password)

if __name__ == "__main__":
    main()

