from datetime import datetime

def days_since(date_str):
    # Try to parse the input date string
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        # Get today's date
        today = datetime.today()
        # Calculate the difference in days
        delta = today - target_date
        return delta.days, target_date
    except ValueError:
        return None, None

def main():
    # Input from the user
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")

    # Calculate days since the date
    days, target_date = days_since(date_str)

    if days is None:
        print("Некорректный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")
    else:
        # Format target date for better readability
        formatted_date = target_date.strftime("%d %B %Y")
        print(f"С {formatted_date} прошло {days} дней.")

if __name__ == "__main__":
    main()
