def count_vowels_consonants(text):
    # Определяем гласные
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    vowel_count = 0
    consonant_count = 0

    # Перебираем каждый символ
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Ввод от пользователя
text = input("Введите текст: ")

# Подсчёт гласных и согласных
vowels, consonants = count_vowels_consonants(text)

print("Количество гласных:", vowels)
print("Количество согласных:", consonants)
