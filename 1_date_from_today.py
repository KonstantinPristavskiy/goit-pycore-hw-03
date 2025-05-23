# to make date objects
from datetime import datetime


def get_days_from_today(date_string: str) -> int | None:
    '''
    функція рахує кількість днів між сьогоднішньою датою і переданою як параметр

    аргументи: рядок у форматі "YEAR-MONTH-DATE"

    повертає: ціле число днів у форматі int, 
    розраховану як різницю між date_string і сьогоднішньою датою
    '''

    try:
        # конвертація рядка в обʼєкт datetime
        date = datetime.strptime(date_string, "%Y-%m-%d")

        # створюємо обʼєкт datetime сьогоднішньої дати
        today_date = datetime.today()

        # розраховуємо різницю між сьогоднішньою датою і заданою, відсікаємо години
        days_from_today = today_date - date
        # перетворюємо в int
        days_from_today = days_from_today.days

        # повертається ціле число в днях
        return days_from_today
    
    # якщо рядок в неправильному форматі
    except ValueError as e:
        print("Date string not in correct format")  
        return None
    


if __name__ == "__main__":

    # визначаємо дату, для якої хочемо порахувати різницю в днях
    date_1 = "2045-05-10"

    # рахуємо різницю в днях
    date_1_diff = get_days_from_today(date_1)

    # виводимо результат
    print(f"Кількість днів між {date_1} і сьогодні: {date_1_diff}")



