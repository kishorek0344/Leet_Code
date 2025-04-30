import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sort_salary = employee['salary'].sort_values(ascending=False).reset_index(drop=True)
    unique_salary = sort_salary.unique()
    if len(unique_salary) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [unique_salary[1]]})
    