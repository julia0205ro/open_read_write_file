import pprint

cook_book = {}

with open('cook_book.txt', encoding='utf-8') as f:
    for line in f.read().split('\n\n'):
        key, *values = line.split('\n')
        values_list = []
        for value in values[1:]:
            values_list.append({'ingredient_name': value.split(' | ')[0],
                                'quantity': value.split(' | ')[1],
                                'measure': value.split(' | ')[2]})
        cook_book[key] = values_list

pprint.pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    all_ingredient = []
    ing_dict_list = []
    for dish in dishes:
        if dish in cook_book:
             for ingredient in cook_book[dish]:
                    igr_dict = {'measure': ingredient['measure'],
                                'quantity': int(ingredient['quantity']) * person_count}
                    ing_dict_list.append(igr_dict)
                    if ingredient['ingredient_name'] not in all_ingredient:
                        all_ingredient.append(ingredient['ingredient_name'])
                    else: 
                        ingredient['ingredient_name'] = f"{ingredient['ingredient_name']} для другого блюда"
                        all_ingredient.append(ingredient['ingredient_name'])
    shop_list = dict(zip(all_ingredient, ing_dict_list))
    return shop_list

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))