import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses['class'].value_counts()
    valid_classes = class_counts[class_counts >= 5].index
    return courses[courses['class'].isin(valid_classes)][['class']].drop_duplicates().sort_values('class').reset_index(drop=True)
