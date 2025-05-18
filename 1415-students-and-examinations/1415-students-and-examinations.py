import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Cross join students and subjects
    all_combinations = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)

    # Step 2: Count exams by student_id and subject_name
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Step 3: Left join to include students who didn't attend exams
    result = all_combinations.merge(exam_counts, on=['student_id', 'subject_name'], how='left')

    # Step 4: Fill NaN with 0 for students who didn't attend any exam
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Step 5: Sort by student_id then subject_name for expected order
    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result
