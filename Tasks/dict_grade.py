# function that takes a dictionary of student names and their grades, and returns the name of the student with the highest grade.
def student(grades):
    highest_grade = -1
    top_name = ""
#max()
    for name in grades_dict:
        grade = grades_dict[name]
        if grade > highest_grade:
            highest_grade = grade
            top_name = name

    return top_name
grades = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 90
}

print(student(grades))  # op: Bob
