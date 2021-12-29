import scraper
import pandas as pd


def create_recipes_id_csv():
    fields = ['id']
    recipes_df = pd.read_csv('RAW_recipes.csv', skipinitialspace=True, usecols=fields)
    recipes_df.to_csv("recipes_id.csv", index=False)


def lessgo():
    df = pd.read_csv("recipes_id.csv")

    for _, row in df.head(15).iterrows():
        url = "https://www.food.com/recipe/" + str(row['id'])
        print(f"\n{url}")

        quantity_from_url = scraper.quantity_from_url(url)
        units_from_url = scraper.units_from_url(url)
        print(f"Quantity list:\t\t\t\t {quantity_from_url}")
        print(f"Units unparsed /w product:\t {units_from_url}")
        print(f"Units parsed /w product:\t {scraper.unit_translation(units_from_url)}")
        print(
            f"Quantity /w amount: \t\t \
            {list(zip(quantity_from_url, scraper.remove_products_from_string(units_from_url)))}")
        print(
            f"Quantity /w amount: \t\t \
            {list(zip(quantity_from_url, scraper.unit_translation(scraper.remove_products_from_string(units_from_url))))}")


def sample():
    url = "https://www.food.com/recipe/44061"
    quantity_from_url = scraper.quantity_from_url(url)
    units_from_url = scraper.units_from_url(url)
    print(f"Quantity list:\t\t\t\t {quantity_from_url}")
    print(f"Units unparsed /w product:\t {units_from_url}")
    print(f"Units parsed /w product:\t {scraper.unit_translation(units_from_url)}")
    print(
        f"Quantity /w amount: \t\t \
        {list(zip(quantity_from_url, scraper.remove_products_from_string(units_from_url)))}")
    print(
        f"Quantity /w amount: \t\t \
        {list(zip(quantity_from_url, scraper.unit_translation(scraper.remove_products_from_string(units_from_url))))}")


if __name__ == '__main__':
    # lessgo()
    sample()
