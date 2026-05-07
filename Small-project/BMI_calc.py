# 💡 Workflow: BMI Calculator (Flask)
# Route 1 – Home page
# Shows a simple HTML form:
# Input ➔ Weight (kg) and Height (cm)
# Route 2 – Result page
# Receives POST data from form
# Calculates BMI = weight / (height/100)^2
# Returns a formatted page:
# Shows BMI value and category ➔ Underweight / Normal / Overweight

from flask import Flask,request

bmi = Flask(__name__)

@bmi.route('/home')
def home():
    return '''
    <form method="POST" action="/result">
        <input type="number" name="weight" placeholder="kg"><br>
        <input type="number" name="height" placeholder="cm"><br>
        <input type="submit" value="Submit"> 
    </form>
    '''

@bmi.route('/result',methods=["POST"])
def result():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight/(height/100)**2
    if bmi >= 30:
        category = "Obese"
    elif bmi >= 25 :
        category = "Overweight"
    elif bmi >= 18.5 :
        category ="Normal"
    else:
        category = "Underweight"
    return f"BMI: {bmi:.2f}\nCategory: {category} "
    

if __name__ == '__main__':
    bmi.run(debug=True)
    
    
    '''
    What im learned: 
    
    POST to send data to backend
    :.2f for limit the number display/format to 2 decimal places
    Use request from Flask to take fetch data from other pages :
    request.form[]
     
    '''