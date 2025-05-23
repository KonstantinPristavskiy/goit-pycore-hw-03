import re


def normalize_phone(phone_number_input: str) -> str | None:
    """
    Перетворює номер у правильний міжнародний формат.
    
    Аргументи: рядок з номером 

    Вивід: рядок з правильним форматом. Якщо довжина номера неправильна 
    або він починається неправильно (має починатись з "+380"), повертає None
    """
    # видаляємо все окрім цифер і знака +
    phone_number = re.sub(r'[^\d+]', '', phone_number_input)

    # якщо номер починається з +380, він вже корректний
    if phone_number.startswith('+380'):
        pass

    # якщо номер починається з 380, додаємо +
    elif phone_number.startswith('380'):
        phone_number = "+" + phone_number

    # в інших випадках додаємо +38
    else:
        phone_number = "+38" + phone_number

    #визначаємо додаткові перевірки, коли номер неправильний (має не 13 символів, або не починається з +380)
    if (len(phone_number) != 13) or (not phone_number.startswith("+380")):
        print(f"Обрахований номер {phone_number} має невірну кількість цифр або починається неправильно.")
        print(f"Його не можна використовувати. Початковий номер: {phone_number_input}")
        return None
    else:
        return phone_number




if __name__ == "__main__":

    # тести різних номерів
    assert normalize_phone("    +38(050)123-32-34") == "+380501233234"
    assert normalize_phone("     0503451234") == "+380503451234"
    assert normalize_phone("(050)8889900") == "+380508889900"
    assert normalize_phone("38050-111-22-22") == "+380501112222"
    assert normalize_phone("38050 111 22 11   ") == "+380501112211"
    assert normalize_phone("+38 (067) 777-77-77") == "+380677777777"
    assert normalize_phone("067 888 99 00") == "+380678889900"
    assert normalize_phone("380671234567") == "+380671234567"
    assert normalize_phone("+380501234567") == "+380501234567"
    assert normalize_phone("03451234") == None
    assert normalize_phone("+501234567") == None
    assert normalize_phone("501234567") == None
    assert normalize_phone("3001234567") == None
    

    raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


