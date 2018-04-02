"""Программа расчета необходимых для готовки блюд ингридиентов."""


def return_shop_list(cook_book, dishes, person_count):
    """Расчет необходимых для покупки ингридиентов."""
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] \
                    = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] \
                    += new_shop_list_item['quantity']
    return shop_list


def return_cook_book():
    """Процедура подготовки книги рецептов."""
    cook_book = {}
    with open('cook_book.txt', encoding='utf8') as our_file:

        finish_reciept = True

        for line in our_file:
            line = line.strip().lower()
            if finish_reciept:
                dish = line
                dish_reciept = []
                finish_reciept = False
                # Строка с количеством ингридиентов
                #  не требуется, поэтому ее пропускаем.
                our_file.readline()
            else:
                if not line:
                    cook_book[dish] = dish_reciept
                    finish_reciept = True
                else:
                    our_ingridient = line.split('|')

                    dish_ingridients = {}
                    dish_ingridients['ingridient_name'] = \
                        our_ingridient[0].strip()
                    dish_ingridients['quantity'] = float(our_ingridient[1])
                    dish_ingridients['measure'] = our_ingridient[2].strip()
                    dish_reciept.append(dish_ingridients)
        cook_book[dish] = dish_reciept

    return cook_book


def return_dishes():
    """Запрашиваем наименование блюд."""
    return input(
        'Введите блюда в расчете на одного человека через запятую: ').\
        lower().split(', ')


def print_shop_list(p_list):
    """Выводим содержимое листа покупок."""
    for p_list_item in p_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**p_list_item))


def main():
    """Основная процедура."""
    person_count = int(input('Введите количество человек: '))
    dishes = return_dishes()
    cook_book = return_cook_book()
    print_shop_list(return_shop_list(cook_book, dishes, person_count))


main()
