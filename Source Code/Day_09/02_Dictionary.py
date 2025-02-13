student_scores = {
    "Harry": 81, 
    "Ron": 78, 
    "Hermoine": 99, 
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


for name, marks in student_scores.items():
    if marks > 90:
        student_grades[name] = "Outstanding"
    elif marks > 80:
        student_grades[name] = "Exceeding Expectations"
    elif marks > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

for name, grade in student_grades.items():
    print(name, end=': ')
    print(grade)