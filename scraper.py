import requests
from bs4 import BeautifulSoup
import re


def quantity_from_url(url):
    # extract quantity classes
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    quantity_divs = soup.find_all("div", class_="recipe-ingredients__ingredient-quantity")

    # strip from tags
    quantity_list = [re.sub('<[^<]+?>', '', str(ingredient)).replace(" ", "") for ingredient in quantity_divs]

    parts_divs = soup.find_all("div", class_="recipe-ingredients__ingredient-parts")

    # strip from tags
    parts_list = [re.sub('<[^<]+?>', '', str(ingredient)).strip() for ingredient in parts_divs]

    return quantity_list, parts_list


def unit_translation(list_of_ingredients):
    unit_translation_to_grams = {
        # volume units (ml)
        "teaspoons": 5,
        "teaspoon": 5,
        "tsp": 5,

        "tablespoons": 15,
        "tablespoon": 15,
        "tbsp": 15,

        "fl. ounce": 30,

        "cups": 240,
        "cup": 240,

        "pints": 473,
        "pint": 473,

        "quarts": 945,
        "quart": 945,

        "gallons": 3785,
        "gallon": 3785,

        # "drops": "drops",
        # "drop": "drop",  # 0.05

        # weight units (g)
        "ounces": 28,
        "ounce": 28,

        "pounds": 454,
        "pound": 454,
        "lbs": 454,
        "lb": 454,
    }

    for key in unit_translation_to_grams.keys():
        list_of_ingredients = [x.lower().replace(key, str(unit_translation_to_grams[key]) + 'g') for x in
                               list_of_ingredients]

    # TODO translate only if in translation dict
    return list_of_ingredients


def remove_products_from_string(list_of_ingredients):
    return [re.sub("\s.*", "", ingredient) for ingredient in list_of_ingredients]
