import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby('player_id',as_index=False)['event_date'].min()
    result.columns = ['player_id', 'first_login']
    return result
    