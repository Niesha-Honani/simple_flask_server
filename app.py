"""Module doe endpoints"""
from flask import Flask, jsonify
from students import Students

app =Flask(__name__)

@app.route('/')
def home():
    """Method for opening page"""
    return "Welcome to the Student Data Page!"

@app.route('/api/raw_student_data/', methods=['GET'])
def api_student_data():
    """Endpoint to retrieve data from student_data function and return as JSON"""
    data = Students.get_student_data()
    return jsonify(data)

@app.route('/api/old_students/', methods=['GET'])
def api_old_student():
    """Method to return old students"""
    student_data = Students.get_student_data()
    old_students = Students.get_old_students(student_data)
    return old_students

@app.route('/api/young_students/', methods=['GET'])
def api_young_student():
    """Method to return young students"""
    student_data = Students.get_student_data()
    young_students = Students.get_younger_students(student_data)
    return young_students

@app.route('/api/advance_students/', methods=['GET'])
def advance_students():
    """Method to return advance students over 21"""
    student_data = Students.get_student_data()
    advanced_students = Students.get_advance_students(student_data)
    return advanced_students

@app.route('/api/student_names/', methods=['GET'])
def student_names():
    """Method to return student names"""
    student_data = Students.get_student_data()
    student_names_list = Students.get_student_names(student_data)
    return student_names_list

@app.route('/api/student_ages/', methods=['GET'])
def student_ages():
    """Method to return ages"""
    student_data = Students.get_student_data()
    ages = Students.get_student_ages(student_data)
    return ages


if __name__ == '__main__':
    app.run(debug=True)
