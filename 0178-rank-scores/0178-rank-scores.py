import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate dense rank with higher scores ranked first
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    # Sort the result by score in descending order
    result = scores.sort_values(by='score', ascending=False)[['score', 'rank']]
    
    return result
