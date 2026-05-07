#Create a Simple JSON API Endpoint
# ✅ Task:
# Build an endpoint /api/sum/<int:a>/<int:b> returning the sum of two numbers in JSON.
#  Convert BMI calculator to JSON API
# ✅ Task:
# Instead of returning as text or HTML, make it return structured JSON:

from flask import Flask,jsonify,request

hello =Flask(__name__)

@hello.route('/api/hello/<name>')
def greet(name):
    data = {"greeting" : f"Hello {name}!!!"}
    return jsonify(data)

@hello.route('/api/sum/form')
def sum_form():
    input = '''
    <form method = "POST" action= "/api/sum">
        <input type = number name= a placeholder=num1><br>
        <input type = number name = b placeholder =num2><br>
        <input type = submit value=Add>
    </form>
    '''
    return input

@hello.route('/api/sum', methods = ["POST"])
def sum():
    a = int(request.form['a'])
    b = int(request.form['b'])
    add = a + b
    add_data = {"a": a , "b" : b, "sum" : add}
    return jsonify(add_data)

@hello.route('/api/bmi')
def bmi():
    input = ''' 
    <form method="POST" action="/api/result">
        <input type=number name=weight placeholder=kg><br>
        <input type=number name=height placeholder=cm><br>
        <input type=submit value=Submit>
    </form>
    '''
    return input 

@hello.route('/api/result', methods=["POST"])
def results():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight/(height/100)**2
    if bmi >= 30 :
        cat = "Obese"
    elif bmi <= 18.5:
        cat = "Underweight"
    elif bmi >= 25 :
        cat = "Overweight"
    else:
        cat= "Normal"
    result_bmi = {
        "weight" : weight,
        "height" : height,
        "bmi" : f"{bmi:.2f}",
        "category" : cat 
    }
    return jsonify(result_bmi)
    
if __name__ == '__main__':
    hello.run(debug=True)

'''
📝 1. What is a Flask JSON API Endpoint?
Instead of returning HTML pages, it returns JSON data that frontend apps or other systems can process.

Example code: 
-----
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def api_hello():
    data = {"message": "Hello, irfn!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
--------
Key Points: 
jsonify() converts dict to proper JSON HTTP response
Use for frontend fetch , mobile Apps / AI intergrations 

'''