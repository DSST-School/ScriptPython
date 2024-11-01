from datetime import datetime

def days_since(date_str):
    """Calculate days since a given date."""
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        delta = today - target_date
        return delta.days, target_date
    except ValueError:
        return None, None

def main():
    while True:
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД (например, 2020-01-01) или 'выход' для завершения: ")
        
        if date_str.lower() == 'выход':
            print("Программа завершена.")
            break
        
        days, target_date = days_since(date_str)

        if days is None:
            print("Некорректный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")
        else:
            if days < 0:
                print("Введенная дата находится в будущем.")
            else:
                formatted_date = target_date.strftime("%d %B %Y")
                print(f"С {formatted_date} прошло {days} дней.")

if __name__ == "__main__":
    main()
