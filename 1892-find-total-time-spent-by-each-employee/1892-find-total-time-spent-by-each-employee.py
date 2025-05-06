import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['emp_id','event_day'], as_index=False)['duration'].sum()
    result.rename(columns={'event_day': 'day', 'duration': 'total_time'}, inplace=True)
    return result
    