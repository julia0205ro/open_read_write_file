from pprint import pprint


def read_file_to_dict(file) -> dict:
    """
    Function for reading text file and
    outputting file contents into a dictionary
    """

    cook_book: dict = {}
    # Create dictionary for ingredients list structure
    names_list: list = ['ingredient_name', 'quantity', 'measure']

    with open(file, 'r', encoding='utf-8') as f:

        # Read every dish in recipes file
        for dish in f.read().split('\n\n'):

            # Extract dish name, ingredients count and ingredients themselves
            dish_name, ingredients_count, *ingredients = dish.split('\n')

            # Create list ingredients as value for dish name
            ingredients_list: list = []
            for ingredient in ingredients:
                ingredients_list.append(dict(zip(names_list, ingredient.split(' | '))))

            # Create dictionary where key is the dish name
            # and value is the ingredients list
            cook_book[dish_name] = ingredients_list

    return cook_book


def get_shop_list_by_dishes(dishes, person_count) -> dict:
    """
    Function that takes dishes from "cook_book" and
    servings count as input,
    returns a dictionary containing ingredient names and
    quantity for the dish
    """

    ingredients_dict: dict = {}

    for dish_name, ingredients_list in read_file_to_dict('recipes.txt').items():
        if dish_name in dishes:
            for ingredient in ingredients_list:

                # Check whether ingredients in dishes match
                if ingredient.get('ingredient_name') not in ingredients_dict.keys():
                    ingredients_dict[ingredient.get('ingredient_name')] = {
                        'quantity': int(ingredient.get('quantity')) * person_count,
                        'measure': ingredient.get('measure')}
                else:
                    ingredients_dict[ingredient.get('ingredient_name')] = {
                        'quantity': int(ingredient.get('quantity'))*person_count +
                                    int(ingredients_dict.get(ingredient.get('ingredient_name')).get('quantity')),
                        'measure': ingredient.get('measure')}

    return ingredients_dict


# Calling functions, printing results
if __name__ == '__main__':

    # Creating cook book
    print('The cook book: ')
    pprint(read_file_to_dict('recipes.txt'))
    print('--------------------')

    # Extracting ingredients from dishes_list for dishes featuring recurring ingredients
    dishes = ['Фахитос', 'Омлет']
    person_count = 3
    print(f"Список блюд: {', '.join(dishes).rstrip()}")
    print(f'На количество персон: {person_count}')
    pprint(get_shop_list_by_dishes(dishes, person_count))
    print('--------------------')

    # Extracting ingredients from dishes_list for ather dishes
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    print(f"Список блюд: {', '.join(dishes).rstrip()}")
    print(f'На количество персон: {person_count}')
    pprint(get_shop_list_by_dishes(dishes, person_count))
