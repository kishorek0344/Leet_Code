import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count direct reports for each manager
    manager_counts = employee['managerId'].value_counts()

    # Filter managers with at least 5 direct reports
    qualifying_managers = manager_counts[manager_counts >= 5].index

    # Get names of these managers using their ID
    result = employee[employee['id'].isin(qualifying_managers)][['name']]
    
    return result
