import scraper
import pandas as pd
import json


def create_recipes_id_csv():
    fields = ['id', 'name', 'ingredients']
    recipes_df = pd.read_csv('RAW_recipes.csv', skipinitialspace=True, usecols=fields)
    recipes_df.to_csv("recipes_id.csv", index=False)


def main():
    df = pd.read_csv("recipes_id.csv")

    unique_units = []
    with open("recipes.json", "a+") as file:
        # data = json.load(file)

        for _, row in df.iterrows():
            url = "https://www.food.com/recipe/" + str(row['id'])

            quantity_from_url, units_from_url = scraper.quantity_from_url(url)

            products_dict = []
            single_recipe_dict = {}

            jsonloaded = eval(row['ingredients'])

            for product in range(len(quantity_from_url)):
                if len(quantity_from_url) != len(jsonloaded):
                    continue

                if quantity_from_url[product]:
                    unit = scraper.remove_products_from_string(units_from_url)[product]
                    single_product_dict = {'product_name': jsonloaded[product], 'quantity': quantity_from_url[product],
                                           'unit': unit}
                    if unit not in unique_units:
                        unique_units.append(unit)

                else:
                    single_product_dict = {'product_name': jsonloaded[product], 'quantity': None,
                                           'unit': 'unit'}

                products_dict.append(single_product_dict)

            single_recipe_dict['url'] = url
            single_recipe_dict['name'] = str(row['name'])
            single_recipe_dict['products'] = products_dict
            file.write(json.dumps(single_recipe_dict) + ",\n")
            print(f"added {url}")

        # recipes_list.append(single_recipe_dict)

    # print(json.dumps(recipes_list, indent=4))


def cleaning_empty_products():
    with open("recipes.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        data = [x for x in data if x['products']]

    with open("recipes.json", "w+", encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2))


def unique_units():
    with open("recipes.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        uniq_units = []
        for recipe in data:
            for product in recipe['products']:
                if product['unit'] not in uniq_units:
                    uniq_units.append(product['unit'])

    with open("unique_units.txt", "w+") as file:
        file.write("\n".join(uniq_units))


def printer(quantity_from_url, units_from_url):
    print(f"Quantity list:\t\t\t\t {quantity_from_url}")
    print(f"Units unparsed /w product:\t {units_from_url}")
    print(f"Units parsed /w product:\t {scraper.unit_translation(units_from_url)}")
    print(
        f"Quantity /w amount: \t\t \
                {list(zip(quantity_from_url, scraper.remove_products_from_string(units_from_url)))}")

    quant_and_translated_units = list(
        zip(quantity_from_url, scraper.unit_translation(scraper.remove_products_from_string(units_from_url))))

    print(
        f"Quantity /w amount: \t\t \
                {quant_and_translated_units}")


def sample():
    url = "https://www.food.com/recipe/67888"
    quantity_from_url, units_from_url = scraper.quantity_from_url(url)
    print(f"\nQuantity list:\t\t\t\t {quantity_from_url}")
    print(f"\nUnits unparsed /w product:\t {units_from_url}")
    print(f"\nUnits parsed /w product:\t {scraper.unit_translation(units_from_url)}")
    print(
        f"\nQuantity /w amount: \t\t \
        {list(zip(quantity_from_url, scraper.remove_products_from_string(units_from_url)))}")
    print(
        f"\nQuantity /w amount: \t\t \
        {list(zip(quantity_from_url, scraper.unit_translation(scraper.remove_products_from_string(units_from_url))))}")


if __name__ == '__main__':
    unique_units()
