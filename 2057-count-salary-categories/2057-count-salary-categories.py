import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Categorize each income into salary category
    accounts['category'] = accounts['income'].apply(
        lambda x: 'Low Salary' if x < 20000 else ('Average Salary' if x <= 50000 else 'High Salary')
    )
    
    # Count occurrences of each category
    counts = accounts['category'].value_counts().reindex(
        ['Low Salary', 'Average Salary', 'High Salary'], fill_value=0
    ).reset_index()
    
    # Rename columns to match expected output
    counts.columns = ['category', 'accounts_count']
    
    return counts
