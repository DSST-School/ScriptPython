def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    return vowel_count, consonant_count

# Ввод от пользователя
text = input("Введите текст: ")

# Подсчёт гласных и согласных
vowels, consonants = count_vowels_consonants(text)

print("Количество гласных:", vowels)
print("Количество согласных:", consonants)
