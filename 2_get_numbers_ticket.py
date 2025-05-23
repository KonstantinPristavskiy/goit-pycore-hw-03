# for random number generation
import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list | None:
    """
    генерує набір унікальних випадкових чисел. 
    
    arguments: min - мінімальне можливе число у наборі (не менше 1).
             max - максимальне можливе число у наборі (не більше 1000).
            quantity - кількість чисел, які потрібно вибрати (значення між min і max).

    
    return: повертає унікальний відсорований випадковий набір чисел у межах заданих параметрів, у форматі list
 
    """

    # checking arguments
    if min < 1:
        print("minimum parameter cannot be less than 1")
        return None
    
    if max > 1000:
        print("maximum parameter cannot be more than 1000")
        return None
    
    if (quantity <= 0) or (quantity > (max - min)):
        print("quantity number is wrong. It should be positive. It should be less than amount of possible numbers")
        return None
    
    # creating an empty set
    random_set = set()

    # iterate until set is full (equals to quantity amount)
    while len(random_set) < quantity:
        random_set.add(random.randint(min, max))

    # change set to list and sort it
    random_list = sorted(list(random_set))


    return random_list




if __name__ == "__main__":



    # визначаємо виграшні комбінації 
    winning_combination = get_numbers_ticket(1, 10, 5)


    # виводимо комбінації
    print(f"Виграшні комбінації: {winning_combination}")


