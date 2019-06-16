
# omniparser/gradebook_parser.py

import os
import statistics
import pandas
import json

## csv module
def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    #breakpoint()

    rows = df.to_dict("records")
    grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    avg_grade = statistics.mean(grades)

    #alternatively
    # avg_grade = df["final_grade"].mean()

    return avg_grade #90.64 #"OOPS"

## json module

##Kyoung's version
#def calculate_average_grade_from_json(my_json_filepath):
#    df = pandas.read_json(my_json_filepath)
#    rows = df.to_dict("records")
#    students = [r["students"] for r in rows] 
#    grades = [s["finalGrade"] for s in students] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
#    avg_grade = statistics.mean(grades)
#    return avg_grade #90.64 #avg_grade #"OOPS"

#Inclass-version
def calculate_average_grade_from_json(x):
    #breakpoint()   # breakpoint is inside def so it will not be get to here unless the main code invoke the defined function
#    return "HEY!!"

    with open(x, "r") as f:
        file_contents = f.read()
    #    print(type(file_contents)) #> str

    gradebook = json.loads(file_contents)

    students = gradebook["students"]
    grades = [s["finalGrade"] for s in students]

    avg_grade = statistics.mean(grades)
#    breakpoint()

    return avg_grade

    #print(type(gradebook))
    #print(gradebook)

#    breakpoint()

#    df = pandas.read_json(my_json_filepath)
#    rows = df.to_dict("records")
#    students = [r["students"] for r in rows] 
#    grades = [s["finalGrade"] for s in students] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
#    avg_grade = statistics.mean(grades)
#    return avg_grade #90.64 #avg_grade #"OOPS"

if __name__ == "__main__":
#    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
#
#    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
#
#    #absolute directory address
#    #gradebook_filepath = "/Users/Kyoung/Documents/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
#
#    #relative directory address => But, this will not work if we change the directory
#    #gradebook_filepath = "data/gradebook_2019.csv"
#
#    #gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")
#
#    avg = calculate_average_grade_from_csv(gradebook_filepath)
#    avg = calculate_average_grade_from_json(gradebook_filepath)
    

# not working
#    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")
    print(gradebook_filepath)
    print(os.path.isfile(gradebook_filepath))
    avg_2019 = calculate_average_grade_from_json(gradebook_filepath)

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
#    print(gradebook_filepath) #>  c:\users\mike\documents\github\omniparser-starter-py\omniparser\gradebook_parser.py
#    print(os.path.isfile(gradebook_filepath)) #> True
    avg_2018 = calculate_average_grade_from_json(gradebook_filepath)
    print("Average Grade of 2018 is: " + str(avg_2018))
    print("Average Grade of 2019 is: " + str(avg_2019))



#    print(avg)


