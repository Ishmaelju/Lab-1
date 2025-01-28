from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!12'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
          if student['pref'] == pref:
             result.append(student)
        return jsonify(result)
    return jsonify(data) 

@app.route('/students/<id>')
def get_student_id(id):
    for student in data:
        if student['id'] == id:
            return jsonify(student) 
    return jsonify({'error': 'Student not found'}), 404

@app.route('/stats')
def get_amount():
   chicken = 0
   fish = 0
   computer_scienceM = 0
   computer_scienceS = 0
   information_techM = 0
   information_techS = 0
   Vegetable =0
   for student in data:
     if student['pref'] == 'Chicken':
        chicken+=1
     if student['pref'] == 'Fish':
        fish+=1
     if student['pref'] == 'Vegetable':
        Vegetable+=1
     if student['programme'] == 'Computer Science (Major)':
        computer_scienceM+= 1
     if student['programme'] == 'Computer Science (Special)':
        computer_scienceS+=1
     if student['programme'] == 'Information Technology (Major)':
        information_techM+=1
     if student['programme'] == 'Information Technology (Special)':
        information_techS+=1

   response = f"""{{
   Chicken:{chicken},
   Computer Science (Major): {computer_scienceM},
   Computer Science (Special): {computer_scienceS},
   Fish:{fish},
   Information Technology (Major):{information_techM},
   Information Technology (Special):{information_techS},
   Vegetable:{Vegetable}
   }}"""

   return response,200, {'Content-Type': 'text/plain'}


@app.route('/add/<int:a>/<int:b>')
def add_numbers(a,b):
    sum = a + b
    return jsonify ({"sum":sum})

@app.route('/subtract/<int:a>/<int:b>')
def subtract_numbers(a,b):
   differnce = a - b
   return jsonify({"Difference":differnce})

@app.route('/multiply/<int:a>/<int:b>')
def multiply_numbers(a,b):
   product = a * b
   return jsonify({"Product":product})
  
@app.route('/divide/<int:a>/<int:b>')
def divide_numbers(a,b):
   quotient = a/b
   return jsonify ({"Quotient":quotient})



app.run(host='0.0.0.0', port=8080, debug=True)
