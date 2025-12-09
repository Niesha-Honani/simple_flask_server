"""Module doe endpoints"""
from flask import Flask, jsonify
from students import get_student_data, get_old_students, get_younger_students, get_advance_students, get_student_names, get_student_ages

app =Flask(__name__)

@app.route('/')
def home():
    """Method for opening page"""
    return "Welcome to the Student Data Page!"

@app.route('/api/raw_student_data/', methods=['GET'])
def api_student_data():
    """Endpoint to retrieve data from student_data function and return as JSON"""
    data = get_student_data()
    return jsonify(data)

@app.route('/api/old_students/', methods=['GET'])
def api_old_student():
    student_data = get_student_data()
    old_students = get_old_students(student_data)
    return jsonify(old_students)

@app.route('/api/young_students/', methods=['GET'])
def api_young_student():
    student_data = get_student_data()
    young_students = get_younger_students(student_data)
    return jsonify(young_students)

@app.route('/api/advance_students/', methods=['GET'])
def advance_students():
    student_data = get_student_data()
    advanced_students = get_advance_students(student_data)
    return jsonify(advanced_students)

@app.route('/api/student_names/', methods=['GET'])
def student_names():
    student_data = get_student_data()
    student_Names = get_student_names(student_data)
    return jsonify(student_Names)

@app.route('/api/student_ages/', methods=['GET'])
def student_ages():
    student_data = get_student_data()
    ages = get_student_ages(student_data)
    return jsonify(ages)


if __name__ == '__main__':
    app.run(debug=True)
