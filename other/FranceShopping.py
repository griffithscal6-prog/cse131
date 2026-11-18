import functools

NAME_INDEX = 0
CATEGORY_INDEX = 1
PRICE_INDEX = 2

category_types = ['Clothing', 'Shoes', 'Bicycle', 'Accessories']

shopping_list = [
    ["Bib Shorts", "Clothing", 92.50],
    ["Roubaix", "Bicycle", 3599.99],
    ["Cycling computer", "Accessories", 394.99],
    ["Helmet", "Accessories", 299.99],
    ["Road Shoes", "Shoes", 144.99],
    ["700c presta tube", "Accessories", 5.25],
    ["Jersey", "Clothing", 25.99],
    ["Multi-Function Tool", "Accessories", 22.99],
    ["Gloves", "Accessories", 8.99],
    ["Cleats", "Shoes", 15.99],
    ["Power Pedals", "Accessories", 999.99],
    ["Socks", "Clothing", 8.50]
]


accessories_list = list(filter(lambda item : item[CATEGORY_INDEX] == "Accessories", shopping_list))
print(accessories_list)

accessories_cost = functools.reduce(lambda total, item : total + item[PRICE_INDEX], accessories_list, 0)
print(accessories_cost)