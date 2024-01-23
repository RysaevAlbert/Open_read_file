import os, pprint
path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path, encoding='utf-8') as cook_file:
    cookbook = {}
    for string in cook_file:
        dish = string.strip()
        ingredients_count = int(cook_file.readline().strip())
        dish_dict = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cookbook[dish] = dish_dict
        cook_file.readline()

print('Задача №1\n________________________________________________________')
pprint.pprint(cookbook)

def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}
    for dishs in dishes:
        for ingredient in cookbook[dishs]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict

print('Задача №2 \n________________________________________________________')
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

file_names = [f for f in os.listdir('sorted') if os.path.isfile(os.path.join('sorted', f))]
file_contents = {}

for file_name in file_names:
    with open(os.path.join('sorted', file_name), 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_name] = {
            'num_lines': len(lines),
            'content': lines
        }

sorted_contents = sorted(file_contents.items(), key=lambda x: x[1]['num_lines'])

with open(os.path.join('sorted', 'result.txt'), 'w', encoding='utf-8') as result_file:
    for file_name, content in sorted_contents:
        result_file.write(f'{file_name}\n{content["num_lines"]}\n')
        result_file.writelines(content['content'])

print('\nЗадача №3 \n________________________________________________________')
print('Готово! Результат записан в файл')
