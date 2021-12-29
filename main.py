from scraper import *
import pandas as pd


def create_recipes_id_csv():
    fields = ['id']
    recipes_df = pd.read_csv('RAW_recipes.csv', skipinitialspace=True, usecols=fields)
    recipes_df.to_csv("recipes_id.csv", index=False)
    # return recipes_df


def lessgo():
    recipes_df =

if __name__ == '__main__':
    create_recipe_id_csv()
    quantity_from_url = quantity_from_url('https://www.food.com/recipe/44061')
    units_from_url = units_from_url('https://www.food.com/recipe/44061')

    print(f"Quantity list:\t\t\t\t {quantity_from_url}")
    print(f"Units unparsed /w product:\t {units_from_url}")
    print(f"Units parsed /w product:\t {unit_translation(units_from_url)}")
    print(f"Quantity /w amount: \t\t {list(zip(quantity_from_url, remove_products_from_string(units_from_url)))}")
