# 'name_recipes
# 'quantity_ingredients'
# 'ingredient_name'
# 'quantity'
# 'measure'
from contextlib import nullcontext
from idlelib.iomenu import encoding
import collections
cook_book = {}
ingridients = {}

def get_recipes_file(filename):
    state_name = 1
    state_quantity_ingredients = 2
    state_ingredients =3

    state = state_name # текущее состояние
    file = open(filename, encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        line=line.strip()
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
    file.close()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):

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
                ingridients[ingredient_name] = (dict(zip(('measure', 'quantity'),(measure, quantity) )))

    #print(f'\n {ingridients}')

    for ingridient in ingridients.keys():
            str = ingridients.get(ingridient)
            quantity = str.get("quantity") * person_count
            measure = str.get('measure')
        #ingredient_name = ingridient.keys()
        #quantity = ingridient.get('quantity')
            ingridients[ingridient] = (dict(zip(('measure', 'quantity'), (measure, quantity))))
    #print(ingridients)
    return ingridients


#print(get_recipes_file('recipes.txt'))
get_recipes_file('recipes.txt')
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
