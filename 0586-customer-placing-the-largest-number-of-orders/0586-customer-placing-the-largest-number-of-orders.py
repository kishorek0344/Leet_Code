import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])  # return empty result
    
    order_counts = orders['customer_number'].value_counts()
    
    if order_counts.empty:
        return pd.DataFrame(columns=['customer_number'])  # also handle if value_counts is empty

    top_customer = order_counts.idxmax()
    
    return pd.DataFrame({'customer_number': [top_customer]})
