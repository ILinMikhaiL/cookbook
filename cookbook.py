# 'name_recipes
# 'quantity_ingredients'
# 'ingredient_name'
# 'quantity'
# 'measure'
from contextlib import nullcontext
from idlelib.iomenu import encoding

cook_book = {}

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
    return cook_book

print(get_recipes_file('recipes.txt'))

