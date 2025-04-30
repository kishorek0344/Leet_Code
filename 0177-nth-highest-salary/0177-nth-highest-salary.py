import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sort_salary = employee['salary'].sort_values(ascending=False)
    uniq_salry = sort_salary.unique()
    if N > len(uniq_salry) or N<=0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        result = uniq_salry[N-1]
        return pd.DataFrame({f"getNthHighestSalary({N})": [result]})
