from datetime import datetime

def days_since(date_str):
    # Преобразуем введенную строку в объект даты
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        # Текущая дата
        today = datetime.today()
        # Расчет разницы в днях
        delta = today - target_date
        return delta.days
    except ValueError:
        return "Некорректный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД."

# Ввод от пользователя
date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")

# Вывод результата
print(f"С этой даты прошло {days_since(date_str)} дней.")
