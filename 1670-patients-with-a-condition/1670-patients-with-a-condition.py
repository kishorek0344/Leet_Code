import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^|\s)DIAB1\d*($|\s)', na=False)][['patient_id', 'patient_name', 'conditions']]
    