from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list:
    """
    визначає, дні народження людей, у яких день народження буде протягом наступних 7 днів. 
    якщо день народження припадає на вихідний, дата привітання переноситься на понеділок

    Аргументи: список словників юзерів у форматі 
    [ {"name": "John Doe", "birthday": "1985.05.25"},  {"name": "Jane Smith", "birthday": "1990.01.01"}]

    повертає: список словників у форматі 
    [{'name': 'Jane Smith', 'congratulation_date': '2025.01.01'}]

    """

    # визначаємо сьогоднішню дату
    today = datetime.today().date()

    # for testing purposes
    #today = datetime(2024, 12, 31).date()

    upcoming_birthdays = []

    for user in users:
        # створюємо змінну birthday, яка дорівнює дню народження юзера
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

         # визначаємо дату народження в цьому році
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # якщо день народження пройшов, маємо розглянути наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  
            
           


        # виводимо різницю між датами
        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            # визначаємо дату привітання
            congratulation_date = birthday_this_year
             
             # перевірка на вихідні (субота = 5, воскресенье = 6)
            if congratulation_date.weekday() >= 5:  
                # переносимо дату привітання на понеділок
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date = congratulation_date + timedelta(days=days_to_monday)
            

            # додаємо в список з днями народженнями
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays





if __name__ == "__main__":
    users = [
    {"name": "John Doe", "birthday": "1985.05.25"},
    {"name": "Jane Smith", "birthday": "1990.01.01"}
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

