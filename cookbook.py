from contextlib import nullcontext
from idlelib.iomenu import encoding
import collections


def get_recipes_file(filename):
    file = open(filename, encoding='utf-8')
    lines = file.readlines()
    cook_book = create_dict_cook_book(lines)
    file.close()
    return cook_book


def create_dict_cook_book(lines):
    cook_book = {}
    state_name = 1
    state_quantity_ingredients = 2
    state_ingredients = 3
    state = state_name  # текущее состояние

    for line in lines:
        line = line.strip()
        if not line: continue
        if state == state_name:
            name_recipes = line
            cook_book[name_recipes] = []
            state = state_quantity_ingredients
        elif state == state_quantity_ingredients:
            quantity_ingredients = int(line)
            state = state_ingredients
        elif state == state_ingredients:
            ingridient = []
            for str in line.split('|'):
                ingridient.append(str.strip())
            ingridient[1] = int(ingridient[1])
            cook_book[name_recipes].append(dict(zip(('ingredient_name', 'quantity', 'measure'), ingridient)))
            quantity_ingredients = quantity_ingredients - 1
            if quantity_ingredients == 0:
                state = state_name
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_recipes_file('recipes.txt')
    ingridients = get_dict_ingridients(cook_book, dishes)
    ingredients_for_cooking = get_amount_ingredients(ingridients, person_count)
    return ingredients_for_cooking


def get_amount_ingredients(ingridients, person_count):
    ingredients_for_cooking = {}
    for ingridient in ingridients.keys():
        str = ingridients.get(ingridient)
        quantity = str.get("quantity") * person_count
        measure = str.get('measure')
        ingredients_for_cooking[ingridient] = (dict(zip(('measure', 'quantity'), (measure, quantity))))
    return ingredients_for_cooking


def get_dict_ingridients(cook_book, dishes):
    ingridients = {}
    for dish in dishes:
        for ingridient in cook_book.get(dish):
            ingredient_name = ingridient.get('ingredient_name')
            measure = ingridient.get('measure')
            quantity = ingridient.get('quantity')

            if ingridients.get(ingredient_name):
                # суммировать при одинаковом ингридиенте
                dict_ingr = ingridients.get(ingredient_name)
                quantity2 = dict_ingr.get('quantity')
                quantity = int(quantity) + int(quantity2)
                ingridients[ingredient_name] = (dict(zip(('measure', 'quantity'), (measure, quantity))))
            else:
                ingridients[ingredient_name] = {}
                ingridients[ingredient_name] = (dict(zip(('measure', 'quantity'), (measure, quantity))))
    return ingridients


if __name__ == "__main__":
    cook_book_txt = get_recipes_file('recipes.txt')
    ingridients_txt = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

    print(cook_book_txt)
    print(ingridients_txt)
