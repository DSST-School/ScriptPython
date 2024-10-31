def is_palindrome(text):
    # Убираем пробелы и переводим все символы в нижний регистр
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# Ввод от пользователя
text = input("Введите строку для проверки на палиндром: ")

# Проверка и вывод результата
if is_palindrome(text):
    print("Эта строка является палиндромом.")
else:
    print("Эта строка не является палиндромом.")
