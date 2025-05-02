import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort first to make sure lowest ID is first
    person.sort_values(by='id', inplace=True)
    
    # Drop duplicates and keep only the first (lowest ID) per email
    person.drop_duplicates(subset='email', keep='first', inplace=True)


    