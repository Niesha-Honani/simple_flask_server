"""Module to hold student data"""
def get_student_data():
    """method to return student data"""
    students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]
    return students

def get_old_students(students):
    older_students_list=[]
    for student in students:
        if student['age'] > 20:
            older_students_list.append(student)

    return older_students_list

def get_younger_students(students):
    younger_students_list=[]
    for student in students:
        if student['age'] < 21:
            younger_students_list.append(student)

    return younger_students_list

def get_advance_students(students):
    advance_students_list = []
    for student in students:
        if student['age'] <21 and student['grade'] == 'A':
            advance_students_list.append(student)
    return advance_students_list

def get_student_names(students):
    student_names = []
    #go through students return firstname.value lastname.value
    for student in students:
        student_names.append(student["first_name"] +' '+ student["last_name"])

    return student_names

def get_student_ages(students):
    student_ages = []
    #go through students return firstname.value lastname.value
    for student in students:
        student_ages.append(student["first_name"] + ' ' + student["last_name"] + ' ' + str(student["age"]))

    return student_ages