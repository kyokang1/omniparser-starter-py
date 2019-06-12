
# omniparser/gradebook_parser.py

import os
import statistics
import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)
    rows = df.to_dict("records")
    grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    avg_grade = statistics.mean(grades)
    return avg_grade #90.64 #"OOPS"

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)


