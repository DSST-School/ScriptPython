def count_words_and_characters(text):
    # Подсчёт слов, разделённых пробелами
    word_count = len(text.split())
    # Подсчёт всех символов, кроме пробелов
    char_count = len(text.replace(" ", ""))
    
    return word_count, char_count

# Ввод от пользователя
text = input("Введите текст: ")

# Подсчёт слов и символов
words, characters = count_words_and_characters(text)

print("Количество слов:", words)
print("Количество символов (без пробелов):", characters)
