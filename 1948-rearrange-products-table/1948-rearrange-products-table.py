import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearrange = products.melt(id_vars=['product_id'],var_name='store',value_name='price')
    rearrange = rearrange[rearrange['price'].notna()]
    return rearrange
    