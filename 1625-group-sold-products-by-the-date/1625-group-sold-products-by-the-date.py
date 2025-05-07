import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date')['product'].agg(
        lambda x: ','.join(sorted(set(x)))
    ).reset_index()

    grouped.rename(columns={'product': 'products'}, inplace=True)

    grouped['num_sold'] = grouped['products'].apply(lambda x: len(x.split(',')))

    grouped = grouped.sort_values('sell_date').reset_index(drop=True)

    # Reorder columns: sell_date, num_sold, products
    return grouped[['sell_date', 'num_sold', 'products']]
