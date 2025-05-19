import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Filter companies named 'RED'
    red_companies = company[company['name'] == 'RED']

    # Step 2: Merge orders with red companies to find orders related to RED
    red_orders = pd.merge(orders, red_companies, on='com_id')

    # Step 3: Get list of sales_ids who sold to RED
    red_sales_ids = red_orders['sales_id'].unique()

    # Step 4: Filter out those salespeople
    result = sales_person[~sales_person['sales_id'].isin(red_sales_ids)]

    # Step 5: Return only the 'name' column
    return result[['name']]
