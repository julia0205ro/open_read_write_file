# Project: Program for Cook Book Featuring Collection of Recipes

Program for managing cook book.  
  
Recipes list's stored in text file in the following format:  
>Dish name  
>Quantity of ingredients in the dish  
>Ingredient name  
>Ingredient quantity  
>Ingredient measure  
  
[Example]()  
  
File may contain an arbitrary number of dishes.  
  
### Task №1  
  
The following dictionary must be generated:  
>cook_book = {  
>  'Омлет': [  
>    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},  
>    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},  
>    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}  
>    ],  
>  'Утка по-пекински': [  
>...  
  
### Task №2  
  
Compose a function that accepts dishes list from cook book and servings count. 
The output must be a dictionary containing ingredients names and their quantities for the dish. 
Ingredients may occur multiple times. The expected result must be as follows:  
>{  
>  'Картофель': {'measure': 'кг', 'quantity': 2},  
>  'Молоко': {'measure': 'мл', 'quantity': 200},  
>  'Помидор': {'measure': 'шт', 'quantity': 4},  
>  'Сыр гауда': {'measure': 'г', 'quantity': 200},  
>  'Яйцо': {'measure': 'шт', 'quantity': 4},  
>  'Чеснок': {'measure': 'зубч', 'quantity': 6}  
>}  
  